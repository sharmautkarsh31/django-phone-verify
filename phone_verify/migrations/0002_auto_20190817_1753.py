# Generated by Django 2.1.11 on 2019-08-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("phone_verify", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="SMSVerification", old_name="otp", new_name="security_code"
        ),
        migrations.RenameField(
            model_name="SMSVerification",
            old_name="session_code",
            new_name="session_token",
        ),
        migrations.AlterField(
            model_name="SMSVerification",
            name="security_code",
            field=models.CharField(max_length=120, verbose_name="Security Code"),
        ),
        migrations.AddField(
            model_name="smsverification",
            name="is_verified",
            field=models.BooleanField(
                default=False, verbose_name="Security Code Verified"
            ),
        ),
        migrations.AlterField(
            model_name="smsverification",
            name="session_token",
            field=models.CharField(max_length=500, verbose_name="Device Session Token"),
        ),
    ]