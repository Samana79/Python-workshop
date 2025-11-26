class Notification:

    def get_notification(self):
        pass


class Instagram(Notification):
    def get_notification(self):
        print("notification from instagram")


class Facebook(Notification):
    def get_notification(self):
        print("Notification from Facebook")


instagram = Instagram()
instagram.get_notification()
facebook = Facebook()
facebook.get_notification()
