import json
from typing import List
from .api_service import FlickAPI, Config


class Devices():
    """ The Devices class. """

    def __init__(self, device_name: str, city: str, city_subdiv: str, street: str, plot: str, building: str, postal: str, branch_name: str, branch_industry: str, otp: str):
        """ Initializes an instance of Devices. """
        self.device_name = device_name
        self.city = city
        self.city_subdiv = city_subdiv
        self.street = street
        self.plot = plot
        self.building = building
        self.postal = postal
        self.branch_name = branch_name
        self.branch_industry = branch_industry
        self.otp = otp


class EGSData:
    """ The EGSData class. """

    def __init__(self, vat_name: str, vat_number: str, devices: List[Devices]):
        """
        Initializes an instance of EGSData.

        Args:
            vat_name (str): The VAT name.
            vat_number (str): The VAT number.
            devices (List[Devices]): A list representing devices.
        """
        self.vat_name = vat_name
        self.vat_number = vat_number
        self.devices = devices

    def to_json(self):

        out = {
            "vat_name": self.vat_name,
            "vat_number": self.vat_number,
        }
        devices = []
        for device in self.devices:
            devices.append(device.__dict__)
        out["devices"] = devices

        return out


class PartyAddId:
    """ The PartyAddId class. """

    def __init__(self, crn: int):
        self.crn = crn


class PartyDetails:
    """ The PartyDetails class. """

    def __init__(self,
                 party_name_ar: str,
                 party_vat: str,
                 city_ar: str,
                 city_subdivision_ar: str,
                 street_ar: str,
                 postal_zone: str,
                 party_add_id: PartyAddId = None,
                 city_en: str = None,
                 city_subdivision_en: str = None,
                 street_en: str = None,
                 plot_identification: str = None,
                 building: str = None,
                 party_name_en: str = None,
                 ):
        self.party_name_ar = party_name_ar
        self.party_name_en = party_name_en
        self.party_vat = party_vat
        self.party_add_id = party_add_id
        self.city_ar = city_ar
        self.city_en = city_en
        self.city_subdivision_ar = city_subdivision_ar
        self.city_subdivision_en = city_subdivision_en
        self.street_ar = street_ar
        self.street_en = street_en
        self.plot_identification = plot_identification
        self.building = building
        self.postal_zone = postal_zone
    def to_json(self):

        out = {
            "party_name_ar" : self.party_name_ar,
            "party_vat" : self.party_vat,
            "city_ar" : self.city_ar,
            "city_subdivision_ar" : self.city_subdivision_ar,
            "street_ar" : self.street_ar,
            "postal_zone" : self.postal_zone,
            "party_add_id" : self.party_add_id,
            "city_en" : self.city_en,
            "city_subdivision_en" : self.city_subdivision_en,
            "street_en" : self.street_en,
            "plot_identification" : self.plot_identification,
            "building" : self.building,
            "party_name_en" : self.party_name_en,
        }
        
        out["party_add_id"] = self.party_add_id.__dict__

        return out


class Invoice:
    """ The Invoice class. """

    def __init__(self, invoice_id: str, issue_date: str, issue_time: str):
        self.id = invoice_id
        self.issue_date = issue_date
        self.issue_time = issue_time


class LineItems:
    """ The LineItems class. """

    def __init__(self,
                 name_ar: str,
                 quantity: float,
                 tax_category: str,
                 tax_exclusive_price: float,
                 tax_percentage: float,
                 name_en: str = None,
                 ):
        self.name_ar = name_ar
        self.name_en = name_en
        self.quantity = quantity
        self.tax_category = tax_category
        self.tax_exclusive_price = tax_exclusive_price
        self.tax_percentage = tax_percentage


class AdvanceInvoices:
    """ The AdvanceInvoices class. """

    def __init__(self,
                 tax_category: str,
                 tax_percentage: float,
                 taxable_amount: float,
                 tax_amount: float,
                 invoices: List[Invoice],):
        self.tax_category = tax_category
        self.tax_percentage = tax_percentage
        self.taxable_amount = taxable_amount
        self.tax_amount = tax_amount
        self.invoices = invoices

    def to_json(self):

        out = {
            "tax_category": self.tax_category,
            "tax_percentage": self.tax_percentage,
            "taxable_amount": self.taxable_amount,
            "tax_amount": self.tax_amount,
        }
        invoices = []
        for invoice in self.invoices:
            invoices.append(invoice.__dict__)
        out["invoices"] = invoices

        return out


class AdvanceDetails:
    """ The AdvanceDetails class. """

    def __init__(self,
                 advance_amount: float,
                 total_amount: float,
                 advance_invoices: AdvanceInvoices
                 ):
        self.advance_amount = advance_amount
        self.total_amount = total_amount
        self.advance_invoices = advance_invoices

    def to_json(self):

        out = {
            "advance_amount":self.advance_amount,
            "total_amount":self.total_amount,
        }
        advance_invoices = []
        for advance_invoice in self.advance_invoices:
            advance_invoices.append(advance_invoice.to_json())
        out["advance_invoices"] = advance_invoices

        return out


class InvoiceData:
    """ The EGSData class. """

    def __init__(self, 
                 egs_uuid: str,
                 invoice_ref_number: str,
                 issue_date: str,
                 issue_time: str,
                 doc_type: str,
                 inv_type: str,
                 payment_method: int,
                 lineitems: LineItems,
                 party_details: PartyDetails,
                 advance_details: AdvanceDetails = None,
                 has_advance: bool = None,
                 currency: str = None,
                 total_tax: str = None,):
        self.egs_uuid = egs_uuid
        self.invoice_ref_number = invoice_ref_number
        self.issue_date = issue_date
        self.issue_time = issue_time
        self.party_details = party_details
        self.doc_type = doc_type
        self.has_advance = has_advance
        self.advance_details = advance_details
        self.inv_type = inv_type
        self.payment_method = payment_method
        self.currency = currency
        self.total_tax = total_tax
        self.lineitems = lineitems

    def to_json(self):

        out = {
            "egs_uuid" : self.egs_uuid,
            "invoice_ref_number" : self.invoice_ref_number,
            "issue_date" : self.issue_date,
            "issue_time" : self.issue_time,
            "doc_type" : self.doc_type,
            "inv_type" : self.inv_type,
            "payment_method" : self.payment_method,
            "has_advance" : self.has_advance,
            "currency" : self.currency,
            "total_tax" : self.total_tax,
        }
        out["party_details"] = self.party_details.to_json()
        lineitems = []
        for lineitem in self.lineitems:
            lineitems.append(lineitem.__dict__)
        out["lineitems"] = lineitems
        out["advance_details"] = self.advance_details.to_json()

        return out


class Bills:
    """
    A class for handling billing operations using the Flick API.

    Args:
        config (Config): A configuration object for the Flick API.

    Attributes:
        api (FlickAPI): An instance of the FlickAPI class with the provided configuration.

    Methods:
        - onboardEGS(egsData: EGSData) -> dict:
            Onboard an EGS  with the provided data.

        - doComplianceCheck(egs_uuid: str) -> dict:
            Perform a compliance check for an EGS with the specified UUID.

        - generateInvoice(invoice_data: InvoiceData) -> dict:
            Generate an invoice based on the provided invoice data.

    """

    def __init__(self, config: Config) -> None:
        """
        Initialize a Bills instance with the provided configuration.

        Args:
            config (Config): A configuration object for the Flick API.
        """
        self.api = FlickAPI(config=config)

    def onboard_egs(self, egs_data: EGSData):
        """
        Onboard an EGS  with the provided data.

        Args:
            egsData (EGSData): Data representing the EGS to be onboarded.

        Returns:
            dict: The response from the API after onboarding the EGS.

        Raises:
            Exception: If an error occurs during the onboarding process.
        """
        try:
            response = self.api.post(
                '/egs/onboard', json.dumps(egs_data.to_json()))
            return response
        except Exception as error:
            # Handle errors here
            raise error

    def do_compliance_check(self, egs_uuid: str):
        """
        Perform a compliance check for an EGS with the specified UUID.

        Args:
            egs_uuid (str): The UUID of the EGS for which compliance is checked.

        Returns:
            dict: The response from the API after performing the compliance check.

        Raises:
            Exception: If an error occurs during the compliance check.
        """
        try:
            response = self.api.get(f"/egs/compliance-check/{egs_uuid}")
            return response
        except Exception as error:
            # Handle errors here
            raise error

    def generate_invoice(self, invoice_data: InvoiceData):
        """
        Generate an invoice based on the provided invoice data.

        Args:
            invoice_data (InvoiceData): Data for generating the invoice.

        Returns:
            dict: The response from the API after generating the invoice.

        Raises:
            Exception: If an error occurs during the invoice generation process.
        """
        try:
            print(json.dumps(invoice_data.to_json()))
            response = self.api.post('/invoice/generate', invoice_data.to_json())
            return response
        except Exception as error:
            # Handle errors here
            raise error
