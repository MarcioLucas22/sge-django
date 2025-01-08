from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow

@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
      """
      Updates the quantity of a product when a new inflow is created.

      This function listens to the post-save signal of the Inflow model.
      If a new inflow instance is created and the quantity is greater than 0,
      it updates the corresponding product's quantity by adding the inflow quantity
      and saves the product.

      Args:
            sender: The model class that sent the signal.
            instance: The instance of the Inflow model that triggered the signal.
            created: A boolean indicating if a new record was created.
            **kwargs: Additional keyword arguments.
      """

      if created:
            if instance.quantity > 0:
                  product = instance.product
                  product.quantity += instance.quantity
                  product.save()