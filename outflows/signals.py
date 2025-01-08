from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow

@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
      """
      Updates the quantity of a product when a new outflow is created.

      This function listens to the post-save signal of the Outflow model.
      If a new outflow instance is created and the quantity is greater than 0 and
      less than or equal to the product's current quantity, it updates the
      corresponding product's quantity by subtracting the outflow quantity
      and saves the product.

      Args:
            sender: The model class that sent the signal.
            instance: The instance of the Outflow model that triggered the signal.
            created: A boolean indicating if a new record was created.
            **kwargs: Additional keyword arguments.
      """
      if created:
            if instance.quantity > 0 and instance.quantity <= instance.product.quantity:
                  product = instance.product
                  product.quantity -= instance.quantity
                  product.save()