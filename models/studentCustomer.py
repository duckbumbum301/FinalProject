from FinalProject.models.Customer import Customer


class studentCustomer(Customer):
    def price(self):
        return super().price()*0.8