from crispy_forms.layout import Layout, Div, Row, Column, Fieldset, Field


class UserCreationFormLayout(Layout):
    """Mise en page pour le formulaire de création
    d'utilisateur"""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Données de connexion",
                Row(
                    Column(Field("name", placeholder="votre nom")),
                    Column(Field("username", placeholder="votre username")),
                ),
                Row(
                    Column(
                        Field("password1", placeholder="Votre mot de passe")),
                    Column(
                        Field(
                            "password2", placeholder="répétez votre mot de passe"
                        )
                    ),
                ),
                style="""
                            border-radius: 10px;
                            margin-bottom: 1rem;
                            background: #DCDCDC;
                        """
            ),
        )

class AddressCreationFormLayout(Layout):
    """Mise en page pour le formulaire de création
    d'adresse"""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Adresses",
                Row(
                    Column("street", css_class="col-md-10"),
                    Column("street_number", css_class="col-md-2"),
                ),
                Row("address_complement"),
                Row(
                    Column("zip_code", css_class="col-md-4"),
                    Column("city"),
                ),
                Row("country"),
                Row("address_type"),
                css_class="fieldset-style"
            )
        )