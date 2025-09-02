
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    public_key = Column(Text)

    # تعریف رابطه برای دسترسی آسان به پیام‌های ارسال و دریافت شده
    sent_messages = relationship("Message", foreign_keys="[Message.sender_id]", back_populates="sender")
    received_messages = relationship("Message", foreign_keys="[Message.recipient_id]", back_populates="recipient")

    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False) # محتوای رمز شده
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    # تعریف رابطه برای دسترسی به فرستنده و گیرنده از طریق شیء پیام
    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_messages")
    recipient = relationship("User", foreign_keys=[recipient_id], back_populates="received_messages")

    def __repr__(self):
        return f"<Message(from={self.sender.username}, to={self.recipient.username})>"

engine = create_engine('sqlite:///chat_app.db')

# ایجاد جداول در پایگاه داده (اگر وجود نداشته باشند)
Base.metadata.create_all(engine)
# ایجاد یک Session برای تعامل با پایگاه داده
Session = sessionmaker(bind=engine)
session = Session()
# --- نمونه عملیات CRUD ---
# Create (ایجاد کاربر جدید)
new_user = User(username='ali', hashed_password='some_hash', public_key='some_key')
session.add(new_user)
session.commit()
# Read (خواندن کاربر)
ali = session.query(User).filter_by(username='ali').first()
print(ali)
# Update (به‌روزرسانی)
ali.public_key = 'new_key'
session.commit()
# Delete (حذف)
session.delete(ali)
session.commit()