class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Plans:
    Plans = { "SSP": {"price": 599, "description": "SSP Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "PP": {"price": 2499, "description": "Professional Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "SEPP": {"price": 9999, "description": "Startup Expo Professional Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "PSP": {"price": 1799, "description": "Premium Student Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "EBC":{"price":149,"description":"Emerge Boot Camp Description","mail_template":"You've successfully enrolled in Emerge! Do join the WhatsApp group using the provided link for further updates and great networking experience. https://chat.whatsapp.com/Gi9DGhmU1mOEOoc4M1qCLv"},
             "TTP": {"price": 1, "description": "Tech team Description","mail_template":" You've successfully enrolled in Emerge! Do join the WhatsApp group using the provided link for further updates and great networking experience. https://chat.whatsapp.com/Gi9DGhmU1mOEOoc4M1qCLv"}}

    def plan_quantity(self, cost):
        array = list(self.Plans.keys())
        for i in array:
            if cost % self.Plans[i]["price"] == 0 and cost >= self.Plans[i]["price"]:
                return i, cost//self.Plans[i]["price"],self.Plans[i]["mail_template"]
        return "TTP", 1,"You've successfully enrolled in Emerge! Do join the WhatsApp group using the provided link for further updates and great networking experience. https://chat.whatsapp.com/Gi9DGhmU1mOEOoc4M1qCLv"    
