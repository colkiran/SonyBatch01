class Employee:
    head1=None
    @classmethod
    def get_companyheadname(cls):
        return cls.head1
    @classmethod
    def set_companyheadname(cls,head1_name):
        cls.head1=head1_name

Employee.set_companyheadname("rohit")
print(Employee.get_companyheadname())

