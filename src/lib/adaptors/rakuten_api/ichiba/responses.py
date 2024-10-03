from __future__ import annotations

from typing import List

from pydantic import BaseModel


class MediumImageUrl(BaseModel):
    imageUrl: str


class SmallImageUrl(BaseModel):
    imageUrl: str


class Item1(BaseModel):
    affiliateRate: int
    affiliateUrl: str
    asurakuArea: str
    asurakuClosingTime: str
    asurakuFlag: int
    availability: int
    catchcopy: str
    creditCardFlag: int
    endTime: str
    genreId: str
    giftFlag: int
    imageFlag: int
    itemCaption: str
    itemCode: str
    itemName: str
    itemPrice: int
    itemPriceBaseField: str
    itemPriceMax1: int
    itemPriceMax2: int
    itemPriceMax3: int
    itemPriceMin1: int
    itemPriceMin2: int
    itemPriceMin3: int
    itemUrl: str  # this is the url to the item page (order page)
    mediumImageUrls: List[MediumImageUrl]
    pointRate: int
    pointRateEndTime: str
    pointRateStartTime: str
    postageFlag: int
    reviewAverage: float
    reviewCount: int
    shipOverseasArea: str
    shipOverseasFlag: int
    shopAffiliateUrl: str
    shopCode: str
    shopName: str
    shopOfTheYearFlag: int
    shopUrl: str
    smallImageUrls: List[SmallImageUrl]
    startTime: str
    tagIds: List[int]
    taxFlag: int


class Item(BaseModel):
    Item: Item1


class ItemResponse(BaseModel):
    GenreInformation: List
    Items: List[Item]
    TagInformation: List
    carrier: int
    count: int
    first: int
    hits: int
    last: int
    page: int
    pageCount: int

    def __str__(self) -> str:
        output = ""
        for item in self.Items:
            output += (
                f"{item.Item.itemName}: {item.Item.itemPrice}円 ({item.Item.itemUrl})\n"
            )
            output += f"====================\n"
        return output


class ErrorResponse(BaseModel):
    error_description: str
    error: str
