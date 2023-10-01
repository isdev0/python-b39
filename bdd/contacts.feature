Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <mobile>, <email>, <email2> and <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | firstname  | lastname  | address  | mobile           | email                | email2               | email3               |
  | FirstName1 | LastName1 | Address1 | +(111)-111-11-11 | email1@email1-sss.rr | email2@email1-sss.rr | email3@email1-sss.rr |
  | FirstName2 | LastName2 | Address2 | +(222) 222 22 22 | email1@email2-sss.rr | email2@email2-sss.rr | email3@email2-sss.rr |
  | FirstName3 | LastName3 | Address3 | +(333)333333     | email1@email3-sss.rr | email2@email3-sss.rr | email3@email3-sss.rr |


Scenario Outline: Update random contact
  Given a non-empty contact list
  Given a contact with <firstname>, <lastname>, <address>, <mobile>, <email>, <email2> and <email3>
  Given a random contact in the list
  When I update a contact in the list with the contact
  Then the new contact list is equal to the old contact list with updated contact

  Examples:
  | firstname         | lastname         | address         | mobile            | email                        | email2                       | email3                       |
  | UpdatedFirstName1 | UpdatedLastName1 | UpdatedAddress1 | +(927)-123-45-678 | updated_email1@email1-rrr.ss | updated_email2@email2-rrr.ss | updated_email3@email3-rrr.ss |


Scenario: Delete random contact
  Given a non-empty contact list
  Given a random contact in the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted