# -*- coding: utf-8 -*-

from sets import Set
from tdm.lib.device import EntityRecognizer, DeviceWHQuery, DddDevice, DeviceAction
from tdm.device_handler import send_to_frontend_device
from chat.contacts import CONTACTS


class ChatDevice(DddDevice):

	def __init__(self):
		self.recogMessage = 0

	class RequestMessageRecog(DeviceAction):
		def perform(self):
			self.device.recogMessage = 1
			return True

	class Call(DeviceAction):
		PARAMETERS = ["selected_contact"]

		@send_to_frontend_device
		def perform(self, selected_contact):
			pass

	class VideoCall(DeviceAction):
		PARAMETERS = ["selected_contact"]

		@send_to_frontend_device
		def perform(self, selected_contact):
			pass

	class SendMessage(DeviceAction):
		PARAMETERS = ["selected_contact", "selected_message"]

		@send_to_frontend_device
		def perform(self, selected_contact, selected_message):
			pass

	class selected_contact(DeviceWHQuery):
		PARAMETERS = ["selected_first_name=''", "selected_last_name=''"]

		def perform(self, first_name_id, last_name_id):
			first_name = first_name_id.replace("first_name_", "", 1)
			last_name = last_name_id.replace("last_name_", "", 1)

			available_contacts = self.device.available_contacts(first_name, last_name)
			result = []
			for contact_id in available_contacts:
				full_name = self.device.full_name_of(contact_id)
				result.append({"value": contact_id, "sort": "contact", "grammar_entry": full_name})
			return result


	class ChatRecognizer(EntityRecognizer):

		def recognize_entity(self, string):
			result = []
			words = string.lower().split()
			if self.device.recogMessage < 1:
				for contact_id, contact in CONTACTS.iteritems():
					first_name = contact["first_name"]
					last_name = contact["last_name"]
					if first_name.lower() in words:
						result.append({"name": "first_name_%s" % first_name, "sort": "first_name", "grammar_entry": first_name.lower()})
					if last_name.lower() in words:
						result.append({"name": "last_name_%s" % last_name, "sort": "last_name", "grammar_entry": last_name.lower()})
			else:
				recognized_entity = {
					"sort": "message",
					"grammar_entry": string
				}
				result.append(recognized_entity)
			self.device.recogMessage -= 1
			return result

	@classmethod
	def number_of(cls, contact_id):
		contact = CONTACTS[contact_id]
		number = contact["number"]
		return number

	@classmethod
	def full_name_of(cls, contact_id):
		contact = CONTACTS[contact_id]
		full_name = "%s %s" % (contact["first_name"], contact["last_name"])
		return full_name

	@classmethod
	def available_contacts(cls, first_name, last_name):
		matching_first_name_contacts = cls.contacts_with_matching_first_name(first_name)
		matching_last_name_contacts = cls.contacts_with_matching_last_name(last_name)
		available_contacts = matching_first_name_contacts.intersection(matching_last_name_contacts)
		return available_contacts

	@classmethod
	def first_available_contact(cls, first_name, last_name):
		available_contacts = cls.available_contacts(first_name, last_name)
		assert len(available_contacts) == 1
		selected_contact = available_contacts.pop()
		return selected_contact

	@classmethod
	def contacts_with_matching_first_name(cls, first_name):
		return cls.contacts_with_matching("first_name", first_name)

	@classmethod
	def contacts_with_matching_last_name(cls, last_name):
		return cls.contacts_with_matching("last_name", last_name)

	@classmethod
	def contacts_with_matching(cls, key, value):
		if not value:
			return Set(CONTACTS.keys())
		return Set([contact_id for contact_id, contact in CONTACTS.iteritems() if contact[key].lower() == value.lower()])

