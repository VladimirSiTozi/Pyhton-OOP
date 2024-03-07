from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(category_id, object_collection):
        return next((o for o in object_collection if o.id == category_id), None)

    def edit_category(self, category_id: int, new_name: str):
        current_category = self.__find_object(category_id, self.categories)
        if current_category:
            current_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = self.__find_object(topic_id, self.topics)
        if current_topic:
            current_topic.topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = self.__find_object(document_id, self.documents)
        if current_document:
            current_document.edit(new_file_name)

    def delete_category(self, category_id):
        current_category = self.__find_object(category_id, self.categories)
        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = self.__find_object(topic_id, self.topics)
        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = self.__find_object(document_id, self.documents)
        if current_document:
            self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = self.__find_object(document_id, self.documents)
        if current_document:
            return current_document.__repr__()

    def __repr__(self):
        result = [d.__repr__() for d in self.documents]
        return '\n'.join(result)
