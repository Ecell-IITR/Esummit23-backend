class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Plans:
    Plans = { "SSP": {"price": 599, "description": "Standard Student Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "PP": {"price": 2499, "description": "Professional Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "SEPP": {"price": 9999, "description": "Startup Expo Professional Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "PSP": {"price": 1799, "description": "Premium Student Pass Description","mail_template":"Venue: Campus, IIT Roorkee"}, 
             "SSEBD": {"price": 2179, "description": "Premium student pass with  SMFD workshop","mail_template":"Venue: Campus, IIT Roorkee"},
             "EBC":{"price":149,"description":"Emerge Boot Camp Description","mail_template":"You've successfully enrolled in Emerge! Do join the WhatsApp group using the provided link for further updates and great networking experience. https://chat.whatsapp.com/Gi9DGhmU1mOEOoc4M1qCLv"},
             "EDP":{"price":249,"description":"Eduquest Description","mail_template":"You've successfully enrolled in Eduquest! Do join the WhatsApp group using the provided link for further updates and great networking experience.https://chat.whatsapp.com/FWEoMFGCzbTHkZNQsNu6uj "},
             "MUND":{"price":1699,"description":"MUN Discount Page","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSPDF":{"price":599,"description":"Standard Student Pass Description First","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSPDS":{"price":499,"description":"Standard Student Pass Description Second","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSPDT":{"price":389,"description":"Standard Student Pass Description Third","mail_template":"Venue: Campus, IIT Roorkee"},
             "PPPDF":{"price":2499,"description":"Professional Pass Description First","mail_template":"Venue: Campus, IIT Roorkee"},
             "PPPDS":{"price":2269,"description":"Professional Pass Description Second","mail_template":"Venue: Campus, IIT Roorkee"},
             "PSPDF":{"price":1799,"description":"Premium Student Pass Discounted First","mail_template":"Venue: Campus, IIT Roorkee"},
             "PSPDS":{"price":1669,"description":"Premium Student Pass Discounted Second","mail_template":"Venue: Campus, IIT Roorkee"},
             "PSPDT":{"price":1499,"description":"Premium Student Pass Discounted Third","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 1489, "description": "Hi-Res Student Pass without accomodation","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 2579, "description": "Hi-Res Student Pass with accomodation","mail_template":"Venue: Campus, IIT Roorkee"},
             "SEPPDF": {"price": 8999, "description": "Startup Expo Professional Pass Discounted First","mail_template":"Venue: Campus, IIT Roorkee"},
             "SEPPDS": {"price": 7949, "description": "Startup Expo Professional Pass Discounted Second","mail_template":"Venue: Campus, IIT Roorkee"},
             "SEPPDT": {"price": 6959, "description": "Startup Expo Professional Pass Discounted Third","mail_template":"Venue: Campus, IIT Roorkee"},
             "SEPPDF": {"price": 5939, "description": "Startup Expo Professional Pass Discounted Fourth","mail_template":"Venue: Campus, IIT Roorkee"},
             "SEEBD": {"price": 8999, "description": "Startup Expo Professional early bird","mail_template":"Venue: Campus, IIT Roorkee"},
             "PSEBD": {"price": 1619, "description": "Premium student early Bird pass","mail_template":"Venue: Campus, IIT Roorkee"},
             "PPEBD": {"price": 2249, "description": "Professional Pass Early bird 10% off","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 539, "description": "Student Standard Early Bird disocunt","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 997, "description": "Student Standard Pass with  SMFD workshop","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 2897, "description": "Professional pass with  SMFD workshop","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 2179, "description": "Premium student pass with  SMFD workshop","mail_template":"Venue: Campus, IIT Roorkee"},
             "SSEBD": {"price": 1879, "description": "Premium student pass with  SMFD workshop Discounted","mail_template":"Venue: Campus, IIT Roorkee"},
             "RDSSP": {"price": 509, "description": "Standard Student Republic Day","mail_template":"<b>HAPPY REPUBLIC DAY !!</b> <br> Venue: Campus, IIT Roorkee"},
             "RDPC": {"price": 2113, "description": "Professional Republic Day Coupon","mail_template":"<b>HAPPY REPUBLIC DAY !!</b> <br> Venue: Campus, IIT Roorkee"},
             "RDPPC": {"price": 1523, "description": "Premium Pass Republic Day","mail_template":"<b>HAPPY REPUBLIC DAY !!</b> <br> Venue: Campus, IIT Roorkee"},
             "RDSEC": {"price": 8467, "description": "Startup Expo Republic Day","mail_template":"<b>HAPPY REPUBLIC DAY !!</b> <br> Venue: Campus, IIT Roorkee"},
    
             "TTP": {"price": 1, "description": "Tech team Description","mail_template":"HAPPY REPUBLIC DAY !! \n Venue: Campus, IIT Roorkee"},
             }

    def plan_quantity(self, cost):
        array = list(self.Plans.keys())
        for i in array:
            if cost % self.Plans[i]["price"] == 0 and cost >= self.Plans[i]["price"]:
                return i, cost//self.Plans[i]["price"],self.Plans[i]["mail_template"]
        return "TTP", 1,"You've successfully enrolled in Eduquest! Do join the WhatsApp group using the provided link for further updates and great networking experience.https://chat.whatsapp.com/FWEoMFGCzbTHkZNQsNu6uj"    
