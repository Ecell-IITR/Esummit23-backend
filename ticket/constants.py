class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"



class Plans:
    Plans = {"MUN": {"price": 1998, "description": "MUN Description"}, "SSP": {"price": 599, "description": "SSP Description"},
             "CDSP": {"price": 1699, "description": "RPSP Description"},"RPSP": {"price": 1499, "description": "RPSP Description"},"PSP": {"price": 1799, "description": "PSP Description"}, "PPP": {"price": 2499, "description": "PPP Description"}, "TTP": {"price": 1, "description": "Tech team Description"}}
    def plan_quantity(self, cost):
        array=list(self.Plans.keys())
        for i in array:
            if cost%self.Plans[i]["price"]==0 and cost >= self.Plans[i]["price"]:
                return i  , cost//self.Plans[i]["price"]
