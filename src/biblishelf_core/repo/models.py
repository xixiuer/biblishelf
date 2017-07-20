import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class Resource(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True )
    uuid = Column(String(64))
    name = Column(String(128))
    create_time = Column(DateTime())

    files = relationship("File", back_populates="resource")


class Repo(Base):
    __tablename__ = "repo"

    id = Column(Integer, primary_key=True)
    uuid = Column(String(64))
    is_local = Column(Boolean)
    paths = relationship("File", back_populates="repo")


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    ed2k = Column(String(32))
    md5 = Column(String(32))
    sha1 = Column(String(150))
    mine_type_id = Column(ForeignKey("mine_type.id"))
    resource_id = Column(ForeignKey("resource.id"))

    resource = relationship("Resource", back_populates="files")
    mine_type = relationship("MineType", back_populates="files")
    paths = relationship("File", back_populates="file")



class MineType(Base):
    __tablename__ = "mine_type"

    id = Column(Integer, primary_key=True)
    mine = Column(String(32))
    full_mine = Column(String(512))
    files = relationship("File", back_populates="mine_type")


class Path(Base):
    __tablename__ = "path"

    id = Column(Integer, primary_key=True)
    path = Column(Text)
    modify_time = Column(DateTime)
    create_time = Column(DateTime)
    file_id = Column(ForeignKey("file.id"))
    repo_id = Column(ForeignKey("repo.id"))
    repo = relationship("Repo", back_populates="paths")
    file = relationship("File", back_populates="paths")