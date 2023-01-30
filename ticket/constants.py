class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


class Plans:
    Plans = {"MUN": {"price": 1998, "description": "MUN Description"}, "SSP": {"price": 599, "description": "SSP Description"},
             "PSP": {"price": 1499, "description": "PSP Description"}, "PPP": {"price": 1999, "description": "PPP Description"}, "TTP": {"price": 1, "description": "Tech team Description"}}
    def plan_quantity(self, cost):
        array=list(self.Plans.keys())
        for i in array:
            if cost%self.Plans[i]["price"]==0 and cost >= self.Plans[i]["price"]:
                return i  , cost//self.Plans[i]["price"]