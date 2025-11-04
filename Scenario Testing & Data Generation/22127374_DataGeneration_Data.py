import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# --- Configuration ---
NUM_CATEGORIES = 500
NUM_INVOICE_ITEMS = 500
OUTPUT_FILENAME = '22127374_DataGeneration_Data.xlsx'

# --- Initialize Faker ---
fake = Faker()

# --- Helper Functions ---
def generate_slug(name):
    """Generates a URL-safe slug from a string."""
    # Updated to handle model codes in parentheses
    return name.lower().replace(' & ', ' ').replace('(', '').replace(')', '').replace(' ', '-')

def generate_model_code():
    """Generates a realistic-looking model code."""
    prefix = random.choice(['Pro', 'HD', 'XT', 'MK-II', 'Series', 'G'])
    number = random.randint(100, 9500)
    return f"({prefix}-{number})"

def generate_tool_category_name():
    """Generates a realistic, tool-shop-themed category name with a model code."""
    tool_types = ['Power Tools', 'Hand Tools', 'Gardening Tools',
                  'Automotive Tools', 'Woodworking', 'Metalworking', 'Plumbing']
    specific_tools = ['Drills', 'Saws', 'Wrenches', 'Hammers', 'Pliers',
                      'Screwdrivers', 'Sockets', 'Clamps', 'Sanders', 'Grinders']
    attributes = ['Heavy Duty', 'Precision', 'Portable', 'Cordless',
                  'Professional', 'DIY']
    suffixes = ['Kits', 'Accessories', 'Supplies', 'Storage', 'Equipment', 'Safety Gear']

    methods = [
        lambda: f"{random.choice(attributes)} {random.choice(specific_tools)}",
        lambda: f"{random.choice(tool_types)} {random.choice(suffixes)}",
        lambda: f"{random.choice(specific_tools)} & {suffixes[random.randint(0, 2)]}",
        lambda: f"Essential {random.choice(tool_types)}",
        lambda: f"{random.choice(specific_tools)} Sets"
    ]
    
    base_name = random.choice(methods)()
    # Append a realistic model code to ensure uniqueness and realism
    model_code = generate_model_code()
    
    return f"{base_name} {model_code}"

# --- 1. Generate 'categories' data ---
print(f"Generating {NUM_CATEGORIES} categories...")
categories_data = []
generated_slugs = set()

for i in range(1, NUM_CATEGORIES + 1):
    # The while loop is now just a safety net for extremely rare collisions.
    # It should run very fast.
    while True:
        name = generate_tool_category_name()
        slug = generate_slug(name)
        if slug not in generated_slugs:
            generated_slugs.add(slug)
            break
    
    # Assign parent_id: 30% chance of having a parent
    parent_id = None
    if i > 1 and random.random() < 0.3:
        parent_id = random.randint(1, i - 1)

    created_at = fake.date_time_between(start_date='-3y', end_date='now')
    updated_at = created_at
    
    categories_data.append({
        'id': i,
        'parent_id': parent_id,
        'name': name,
        'slug': slug,
        'created_at': created_at,
        'updated_at': updated_at
    })

print("Categories generation complete.")


# --- 2. Generate 'invoice_items' data ---
print(f"\nGenerating {NUM_INVOICE_ITEMS} invoice items...")
invoice_items_data = []

for i in range(1, NUM_INVOICE_ITEMS + 1):
    created_at = fake.date_time_between(start_date='-2y', end_date='now')
    updated_at = created_at
    
    invoice_items_data.append({
        'id': i,
        'invoice_id': random.randint(1, 100),
        'product_id': random.randint(1, 50),
        'unit_price': round(random.uniform(10.00, 500.00), 2),
        'quantity': random.randint(1, 10),
        'created_at': created_at,
        'updated_at': updated_at
    })
    
print("Invoice items generation complete.")


# --- 3. Export to Excel ---
print(f"\nExporting data to {OUTPUT_FILENAME}...")
try:
    with pd.ExcelWriter(OUTPUT_FILENAME) as writer:
        categories_df = pd.DataFrame(categories_data)
        invoice_items_df = pd.DataFrame(invoice_items_data)

        categories_df.to_excel(writer, sheet_name='categories', index=False)
        invoice_items_df.to_excel(writer, sheet_name='invoice_items', index=False)
    
    print(f"\nSuccessfully created {OUTPUT_FILENAME} with two sheets: 'categories' and 'invoice_items'.")

except Exception as e:
    print(f"\nAn error occurred while writing to the Excel file: {e}")
