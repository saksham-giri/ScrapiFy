from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0002_scrap_status"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("booked_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="pending", max_length=20)),
                ("buyer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bookings", to=settings.AUTH_USER_MODEL)),
                ("scrap", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bookings", to="listings.scrap")),
            ],
        ),
        migrations.AddConstraint(
            model_name="booking",
            constraint=models.UniqueConstraint(fields=("scrap", "buyer"), name="unique_buyer_scrap_booking"),
        ),
    ]
