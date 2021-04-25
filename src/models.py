from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
from pydantic.color import Color
from typing import Optional


def member_factory(
    workspace: WorkspaceReference,
    *,
    identity: IdentityReference,
    role: str = "Guest",
    status: str = "Active",
    ) -> Member:
    return Member(
        id_=uuid4(),
        workspace=workspace,
        identity=identity,
        role=WorkspaceRole(role),
        status=ResourceStatus(status),
        notification=True,
        channels=(),
    )


class Batch(BaseModel):
    """
    id                  PK
    sku_id              foreginkey int
    purchase_order      integerfield
    material_handle     integerfiled  numbers of materials moved
    manufactured_date   datetime
    expiry_date         datetime
    """
    id: int
    sku_id: int
    purchase_order: int
    material_handle: int
    manufactured_date: datetime
    expiry_date: datetime  # check whether

    @validator("manufactured_date")
    def manufactured_within_five_years(cls, manufactured_date):
        time_in_delta = datetime.now() - manufactured_date
        if not abs(time_in_delta.days) <= 5 * 365:
            raise ValueError(
                "Must be manufactured not exceeding five years from now")
        return manufactured_date

    class Config:
        title = 'Batch'

    def update(self, mapping: typing.Dict[str, typing.Any]) -> Batch:
        return self.copy(update=mapping)

    def add_order(self, channel: ChannelReference) -> Member:
        channels = set(self.channels)
        channels.add(channel)
        return self.copy(update={"channels": tuple(channels)})

    def add_channels(self, channels: typing.Tuple[ChannelReference]) -> Member:
        _channels = set(self.channels) | channels
        return self.copy(update={"channels": tuple(_channels)



class Sku(BaseModel):
    """
    id          charfield
    product     foreginkey
    color       charfield color in pydantic
    size        charfield

    """
    id: int
    product: int
    color: Color
    size: str

    class Config:
        title='SKU'


class Product(BaseModel):
    """
    id                  primarykey      int
    category            foreginkey      int
    batch               foreginkey      int
    name                charfield       str
    price               positive        int
    description         textfield       str
    slug                slugfield       HttpUrl
    brand               foreginkey      int
    status              Boolean         bool
    manufatured_date    datetimefield   datetime    moved to batch
    updated_date        datetime        datetime
    # batch: int
    # price: int

    """
    id: int
    category: int
    name: str
    description: str
    slug: HttpUrl
    brand: str
    status: bool
    updated_date: Optional[datetime]=None

    @ validator('name')
    def check_name_length(cls, name):
        if (len(name) < 3):
            raise ValueError('Name too short!!!')
        return name

    class Config:
        title='Product'


class Category(BaseModel):
    """
    id              primarykey
    name            charfield
    sub_category    foreginkey self numm=true blank=true
    """
    id: int
    name: str
    sub_category: int

    class Config:
        title='Category'


class Unit(BaseModel):
    """
    id              PK
    total_unit      PositiveIntegerField
    name/label/title
    """
    id: int
    total_unit: int
    label: str

    class Config:
        title='Unit'
