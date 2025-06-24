# from easyocr import Reader
from fastapi import BackgroundTasks, FastAPI, status
from pydantic import BaseModel, Field

from mumbai import extract as extract_mumbai
from rural_maharashtra import extract as extract_maharashtra_rural
from urban_maharashtra import extract as extract_maharashtra_urban
from document_number import extract as extract_document


app = FastAPI()


# class UrbanPropertyRequest(BaseModel):
#     start_year: int = Field(default=1995)
#     district: str = Field()
#     village: str = Field()
#     village_name: str = Field()
#     property_no: int = Field()


class UrbanPropertyRequest(BaseModel):
    start_year: int = Field(default=1995)
    district: str = Field()
    district_english: str = Field()
    village: str = Field()
    village_name: str = Field()
    property_no: int = Field()


class RuralPropertyRequest(UrbanPropertyRequest):
    tehsil: str = Field()


class SRODocumentRequest(BaseModel):
    year: int = Field()
    district: str = Field()
    sro: str = Field()
    start_doc_no: int = Field()
    end_doc_no: int = Field()


@app.post("/api/v1/extract/mumbai", status_code=status.HTTP_202_ACCEPTED)
def extract_mumbai_properties(property: UrbanPropertyRequest, background_tasks: BackgroundTasks):
    print(f"Received request: {property}")
    # model = Reader(['en'])
    background_tasks.add_task(
        # extract_mumbai, property.start_year, property.district, property.village, property.village_name, property.property_no)
        extract_mumbai, property.start_year, property.district, property.district_english, property.village, property.village_name, property.property_no)
    return {"message": "Started extraction"}


@app.post("/api/v1/extract/maharashtra/rural", status_code=status.HTTP_202_ACCEPTED)
def extract_rural_maharashtra_properties(property: RuralPropertyRequest, background_tasks: BackgroundTasks):
    print(f"Received request: {property}")
    # model = Reader(['en'])
    background_tasks.add_task(extract_maharashtra_rural, property.start_year,
                              property.district, property.tehsil, property.village,
                              property.property_no)
    return {"message": "Started extraction"}


@app.post("/api/v1/extract/maharashtra/urban", status_code=status.HTTP_202_ACCEPTED)
def extract_urban_maharashtra_properties(property: UrbanPropertyRequest, background_tasks: BackgroundTasks):
    print(f"Received request: {property}")
    # model = Reader(['en'])
    background_tasks.add_task(extract_maharashtra_urban, property.start_year,
                              property.district, property.village, property.property_no)
    return {"message": "Started extraction"}


@app.post("/api/v1/extract/document_number", status_code=status.HTTP_202_ACCEPTED)
def extract_document_number(sro_documents: SRODocumentRequest, background_tasks: BackgroundTasks):
    print(f"Received request: {sro_documents}")
    # model = Reader(['en'])
    background_tasks.add_task(extract_document, sro_documents.year, sro_documents.district, sro_documents.sro,
                              sro_documents.start_doc_no, sro_documents.end_doc_no)
    return {"message": "Started extraction"}