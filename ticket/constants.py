class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Plans:
    Plans = { "SSP": {"price": 599, "description": "SSP Description","mail_templete":" whatsapp link for the group "}, "PP": {"price": 2499, "description": "Professional Pass Description","mail_templete":" whatsapp link for the group "}, 
             "SEPP": {"price": 9999, "description": "Startup Expo Professional Pass Description","mail_templete":" whatsapp link for the group "}, "PSP": {"price": 1799, "description": "Premium Student Pass Description","mail_templete":" whatsapp link for the group "}, 
             "TTP": {"price": 1, "description": "Tech team Description","mail_templete":" whatsapp link for the group"}}

    def plan_quantity(self, cost):
        array = list(self.Plans.keys())
        for i in array:
            if cost % self.Plans[i]["price"] == 0 and cost >= self.Plans[i]["price"]:
                return i, cost//self.Plans[i]["price"],self.Plans[i]["mail_template"]
