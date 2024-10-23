import pandas as pd
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from dbapp.models import Medicine


class Command(BaseCommand):
    help = "Import medicine data from a CSV file"

    def handle(self, *args, **kwargs):
        data_dir = os.path.join(settings.BASE_DIR, "..", "data")
        csv_file_path = os.path.join(data_dir, "medicine.csv")

        try:
            df = pd.read_csv(csv_file_path)
            self.stdout.write(self.style.SUCCESS("Medicine data imported successfully"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File '{csv_file_path}' not found"))
            return

        for _, row in df.iterrows():
            Medicine.objects.create(
                brand_id=row["brand id"],
                brand_name=row["brand name"],
                type=row["type"],
                slug=row["slug"],
                dosage=row["dosage form"],
                genric=row["generic"],
                strength=row["strength"],
                manufacturers=row["manufacturer"],
                package_container=row["package container"],
                package_size=row["Package Size"],
            )

        self.stdout.write(self.style.SUCCESS("Medicine data saved to database"))
