from db import *


class Region(db.Model):
    __tablename__ = 'tb_region'

    id = db.Column(db.Integer, primary_key=True, comment='区域编号')
    name = db.Column(db.String(100), default='', comment='区域名称')
    parent_id = db.Column(db.Integer, db.ForeignKey('tb_region.id'), nullable=True, comment='区域上级id')
    # 在自关联关系中，SQLAlchemy 需要知道哪个字段是外键引用的远端列。
    # remote_side 参数用于明确这个引用关系。它告诉 SQLAlchemy，在这个自关联关系中，哪一侧的列是外键引用的目标。

    children = db.relationship('Region', uselist=True, backref=backref('parent', uselist=False, remote_side=[id]),
                               lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent_id': self.parent_id,
            'children': [child.to_dict() for child in self.children.all()]
        }
