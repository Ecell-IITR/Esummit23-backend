class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Plans:
    Plans = {"TTP": {"price": 1998, "description": "Tech team Description"},"MUN": {"price": 1998, "description": "MUN Description"}, "SSP": {"price": 599, "description": "SSP Description"},
             "PSP": {"price": 1499, "description": "PSP Description"}, "PPP": {"price": 1999, "description": "PPP Description"}}
    def plan_quantity(self, cost):
    
        for i in list(Plans.keys()):
            if cost%self.Plans[i]["price"]==0:
                return i , cost//self.Plans[i]