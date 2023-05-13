from itertools import islice


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            po_box = PostOffice(['a', 'b'])
            message_id = po_box.send_message('a', 'b', 'Hello!')
            len(po_box.boxes['b'])
            1
            message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, N=None):
        """
        read the messages of a certain user

            Args:
                user (str): the user's name.
                N (int): number of messages wanted.
            Returns:
                list: N messages that the user has


            Examples:
                a user has number of messages and he wants
                to read them.

                po_box = PostOffice(['a', 'b'])
                po_box.send_message('a', 'b', 'Hello!')
                po_box.send_message('a', 'b', 'How are you?')
                po_box.send_message('a', 'b', 'nahh bru')
                po_box.send_message('a', 'b', 'you here?')
                print(po_box.read_inbox('b'))

                ['Hello!', 'How are you?', 'nahh bru', 'you here?']

                print(po_box.read_inbox('b', 2))

                ['Hello!', 'How are you?']




        """
        if user not in self.boxes:
            return []

        messages = self.boxes[user]
        if N is None:
            N = len(messages)

        result = []
        for msg in messages[:N]:
            message_details = {
                'id': msg['id'],
                'title': msg['title'],
                'body': msg['body'],
                'sender': msg['sender']
            }
            result.append(message_details)

        return result

    def search_inbox(self, user, wanted):
        """
            search the inbox of a user depending on a given string

                Args:
                    user (str): the user's name.
                    wanted (str): the string to search for in messages.
                Returns:
                    list: all messages that contain wanted in them


                Examples:
                    a user has number of messages and he wants
                    look for messages containing 'you' in them

                    po_box = PostOffice(['a', 'b'])
                    po_box.send_message('a', 'b', 'Hello!')
                    po_box.send_message('a', 'b', 'How are you?')
                    po_box.send_message('a', 'b', 'nahh bru')
                    po_box.send_message('a', 'b', 'you here?')
                    print(po_box.search_inbox('b', 'you'))

                    ['How are you?', 'you here?']


            """
        messages = self.read_inbox(user)
        result = []
        for msg in messages:
            if wanted.lower() in msg['body'].lower() or wanted.lower() in msg['title'].lower():
                result.append(msg)
        return result
