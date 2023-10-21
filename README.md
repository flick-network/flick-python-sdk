# Flick Python SDK
![Platform](https://img.shields.io/badge/python-3-blue)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE.md)


A python interface for interacting with the APIs of Flick.

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Examples](#examples)
- [Contribute to our SDK](#contributing)
- [License](#license)
- [Support](#support)

## Installation
To use the Flick Python SDK in your project, you can install it via pip:

```bash
pip install flick-python-sdk
```

## Getting Started
Before using the package, you need to configure it with your API credentials. You should have an apiKey and specify whether you are using the 'sandbox' or 'production' environment.

Here's how you to initiate our SDK in your project:

```python
import asyncio
from flick import Config
from bills import Bills

config = Config('sandbox', 'your-api-key')
api = Bills(config=config)
```

## Documentation
To learn about available methods and their usage, please refer to the [official API documentation](https://docs.flick.network/).
Here's a glimpse to our Bills Module:

### Bills Client
The Bills client provides access to various functionalities for managing bills. You can interact with the following API endpoints:

#### Onboard EGS to ZATCA:

```python
egs_data = { /* Your EGS data - Check Documentation */ }
loop = asyncio.get_event_loop()
result = loop.run_until_complete(api.onboard_egs(egs_data=egs_data))
```

#### Compliance Check:

```python
egs_uuid = 'your-egs-uuid';
loop = asyncio.get_event_loop()
result = loop.run_until_complete(api.do_compliance_check(egs_uuid))
```

#### Generate E-Invoice for Phase-2 in Saudi Arabia:
```python
invoiceData = { /* Your invoice data - Check Documentation */ }
loop = asyncio.get_event_loop()
result = loop.run_until_complete(api.generate_invoice(invoiceData))
```

## Examples

1. Here's an Example of how you can **onboard multiple EGS to ZATCA Portal** [If you are onboarding PoS devices or VAT-Group members, this comes handy].

2. Examples are included in the examples folder as well

```python
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
 
```

2. Here's an Example of how you can **Genereate a ZATCA-Complied E-Invoice**.

```python
import asyncio
from flick.api_service import Config
from flick.bills import Bills, InvoiceData, PartyAddId, PartyDetails, AdvanceDetails, AdvanceInvoice, Invoice, LineItem

config = Config('sandbox', 'your-api-key')

client = Bills(config)
invoice_data = InvoiceData(
    egs_uuid='7b9cc231-0e14-4bff-938c-4603fe10c4bc',
    invoice_ref_number='INV-5',
    issue_date='2023-01-01',
    issue_time='01=40=40',
    party_details=PartyDetails(
        party_name_ar='شركة اختبار',
        party_vat='300001111100003',
        party_add_id=PartyAddId(
            crn=45463464
        ),
        city_ar='جدة',
        city_subdivision_ar='حي الشرفية',
        street_ar='شارع الاختبار',
        plot_identification='1234',
        building='1234',
        postal_zone='12345',
    ),
    doc_type='388',
    inv_type='standard',
    payment_method=10,
    currency='SAR',
    total_tax=142.,
    has_advance=True,
    advance_details=AdvanceDetails(
        advance_amount=575,
        total_amount=2875,
        advance_invoices=[
            AdvanceInvoice(
                tax_category='S',
                tax_percentage=0.15,
                taxable_amount=500,
                tax_amount=75,
                invoices=[
                    Invoice(
                        invoice_id='INV-1',
                        issue_date='2022-12-10',
                        issue_time='12=28=17',
                    ),
                ],
            ),
        ],
    ),
    lineitems=[
        LineItem(
            name_ar='متحرك',
            quantity=1,
            tax_category='S',
            tax_exclusive_price=750,
            tax_percentage=0.15,
        ),
        LineItem(
            name_ar='حاسوب محمول',
            quantity=1,
            tax_category='S',
            tax_exclusive_price=1750,
            tax_percentage=0.15,
        ),
    ],
)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(client.generate_invoice(invoice_data=invoice_data))
# Process the result the way you want
print(result)

```

## Contributing

We welcome contributions from the community. If you find issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please contact our support team at support@flick.network

## Keywords 

einvoicing, e-invoicing, zatca, phase2, saudi, ksa, fatoora, saudiarabia, egs
