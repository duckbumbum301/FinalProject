from FinalProject.models.Customer import Customer


class normalCustomer(Customer):
    def price(self):
        return super().price()