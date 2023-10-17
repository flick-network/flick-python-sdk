import asyncio
from flick.api_service import Config 
from flick.bills import Bills,EGSData,Device

config = Config('sandbox', 'your-api-key')

client = Bills(config)

egs_data = EGSData(
    vat_name='Test Co.',
    vat_number='300000000000003',
    devices=[
        Device(
            device_name='TestEGS1',
            city='Riyadh',
            city_subdiv='Test Dist.',
            street='Test St.',
            plot='1234',
            building='1234',
            postal='12345',
            # This will be 10-digit TIN if you are onboarding a VAT-Group Member
            branch_name='Riyad Branc   h 1',
            branch_industry='Retail',
            otp='123321',
        ), Device(
            device_name='TestEGS2',
            city='Riyadh',
            city_subdiv='Test Dist.',
            street='Test St.',
            plot='1234',
            building='1234',
            postal='12345',
            # This will be 10-digit TIN if you are onboarding a VAT-Group Member
            branch_name='Riyad Branch 1',
            branch_industry='Retail',
            otp='123321',
        ),
    ]
)


loop = asyncio.get_event_loop()
result = loop.run_until_complete(client.onboard_egs(egs_data=egs_data))
# Process the result the way you want
print(result)
 