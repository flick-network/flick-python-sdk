from flick.api_service import Config
from flick.bills import Bills, InvoiceData, PartyAddId, PartyDetails, AdvanceDetails, AdvanceInvoices, Invoice, LineItems

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
            AdvanceInvoices(
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
        LineItems(
            name_ar='متحرك',
            quantity=1,
            tax_category='S',
            tax_exclusive_price=750,
            tax_percentage=0.15,
        ),
        LineItems(
            name_ar='حاسوب محمول',
            quantity=1,
            tax_category='S',
            tax_exclusive_price=1750,
            tax_percentage=0.15,
        ),
    ],
)

response = client.generate_invoice(invoice_data=invoice_data)
print(response.text)
