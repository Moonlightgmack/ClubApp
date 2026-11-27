from pydantic import BaseModel, ConfigDict, Field


class ClubCreation(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nom: str = Field(min_length=3, max_length=60, examples=["Club cinéma"])
    description: str = Field(default="", max_length=300)
    capacite: int = Field(ge=2, le=200, examples=[20])


class ClubLecture(BaseModel):
    id: int
    nom: str
    description: str
    capacite: int
    nb_membres: int
    places_restantes: int


class AdhesionCreation(BaseModel):
    id_utilisateur: int = Field(gt=0)


class AdhesionLecture(BaseModel):
    id_utilisateur: int
    id_club: int