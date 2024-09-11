from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet
import os

def calculate_tax(net_amount, place_of_supply, place_of_delivery):
    tax_rate = 0.18 
    if place_of_supply == place_of_delivery:
        cgst = sgst = net_amount * (tax_rate / 2)
        return {'CGST': cgst, 'SGST': sgst}
    else:
        igst = net_amount * tax_rate
        return {'IGST': igst}

def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return True

def generate_invoice(seller_details, billing_details, items, place_of_supply, place_of_delivery, signature_path):
    check_file_exists(signature_path)

    file_name = "invoice.pdf"
    document = SimpleDocTemplate(file_name, pagesize=A4)

    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("INVOICE", styles['Title'])
    elements.append(title)

    seller_info = f"Seller Name: {seller_details['name']}<br/>Address: {seller_details['address']}"
    seller = Paragraph(seller_info, styles['Normal'])
    elements.append(seller)

    billing_info = f"Bill To: {billing_details['name']}<br/>Address: {billing_details['address']}"
    billing = Paragraph(billing_info, styles['Normal'])
    elements.append(billing)

    data = [['Description', 'Quantity', 'Unit Price', 'Discount', 'Net Amount', 'Tax Type', 'Tax Amount', 'Total Amount']]

    for item in items:
        net_amount = (item['unit_price'] * item['quantity']) - item['discount']
        taxes = calculate_tax(net_amount, place_of_supply, place_of_delivery)
        tax_type = ', '.join(taxes.keys())
        tax_amount = sum(taxes.values())
        total_amount = net_amount + tax_amount

        data.append([
            item['description'], item['quantity'], f"${item['unit_price']:.2f}", f"${item['discount']:.2f}",
            f"${net_amount:.2f}", tax_type, f"${tax_amount:.2f}", f"${total_amount:.2f}"
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    try:
        signature = Image(signature_path, 100, 50)
        elements.append(signature)
    except Exception as e:
        print(f"Error adding signature image: {e}")

    document.build(elements)
    print(f"Invoice saved as {file_name}")

seller_details = {'name': 'ABC Pvt Ltd', 'address': '123, Business Street, City, State, 456789'}
billing_details = {'name': 'Customer XYZ', 'address': '789, Home Street, City, State, 123456'}
items = [
    {'description': 'Product 1', 'quantity': 2, 'unit_price': 100, 'discount': 10},
    {'description': 'Product 2', 'quantity': 1, 'unit_price': 200, 'discount': 20},
]
place_of_supply = "State A"
place_of_delivery = "State A"
signature_path = "Signature.png" 

try:
    generate_invoice(seller_details, billing_details, items, place_of_supply, place_of_delivery, signature_path)
except FileNotFoundError as e:
    print(e)
