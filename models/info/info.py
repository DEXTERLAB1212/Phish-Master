from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Define the Info model
class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    browser = db.Column(db.String(100), nullable=False)
    geolocation_longitude = db.Column(db.Float, nullable=True)
    geolocation_latitude = db.Column(db.Float, nullable=True)
    geolocation_google_map_link = db.Column(db.String(200), nullable=True)
    isp = db.Column(db.String(100), nullable=True)
    proxy = db.Column(db.Boolean, nullable=False, default=False)
    operating_system = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_agent = db.Column(db.String(200), nullable=True)
    touch_screen = db.Column(db.Boolean, nullable=False, default=False)
    platform = db.Column(db.String(100), nullable=True)
    hostname = db.Column(db.String(100), nullable=True)
    language = db.Column(db.String(50), nullable=True)
    time_zone = db.Column(db.String(50), nullable=True)
    incognito = db.Column(db.Boolean, nullable=False, default=False)
    screen_size = db.Column(db.String(50), nullable=True)
    gpu = db.Column(db.String(100), nullable=True)
    location_from_isp_ip = db.Column(db.String(200), nullable=True)
    user_time = db.Column(db.String(50), nullable=True)
    cpu = db.Column(db.String(100), nullable=True)
    ram = db.Column(db.String(100), nullable=True)
    available_disk_space = db.Column(db.String(100), nullable=True)
    installed_plugins = db.Column(db.Text, nullable=True)
    ad_blocker_enabled = db.Column(db.Boolean, nullable=False, default=False)
    webcam_access = db.Column(db.Boolean, nullable=False, default=False)
    microphone_access = db.Column(db.Boolean, nullable=False, default=False)
    local_ip_address = db.Column(db.String(50), nullable=True)
    public_ip_address = db.Column(db.String(50), nullable=True)
    vpn = db.Column(db.Boolean, nullable=False, default=False)
    timezone_offset = db.Column(db.String(50), nullable=True)
    browser_window_size = db.Column(db.String(50), nullable=True)
    device_model = db.Column(db.String(100), nullable=True)
    device_manufacturer = db.Column(db.String(100), nullable=True)
    bluetooth_status = db.Column(db.Boolean, nullable=False, default=False)
    nfc_status = db.Column(db.Boolean, nullable=False, default=False)
    gyroscope_data = db.Column(db.String(200), nullable=True)
    accelerometer_data = db.Column(db.String(200), nullable=True)
    orientation = db.Column(db.String(50), nullable=True)
    timezone_name = db.Column(db.String(50), nullable=True)
    hardware_concurrency = db.Column(db.Integer, nullable=True)
    memory = db.Column(db.String(50), nullable=True)
    connection_speed = db.Column(db.String(50), nullable=True)
    online_status = db.Column(db.Boolean, nullable=False, default=True)
    notification_permissions = db.Column(db.String(50), nullable=True)
    battery_charging_status = db.Column(db.Boolean, nullable=False, default=False)
    dark_mode_enabled = db.Column(db.Boolean, nullable=False, default=False)
    media_devices = db.Column(db.Text, nullable=True)
    language_preferences = db.Column(db.String(200), nullable=True)
    clipboard_access = db.Column(db.Boolean, nullable=False, default=False)
    idle_time = db.Column(db.String(50), nullable=True)
    dns_prefetching = db.Column(db.Boolean, nullable=False, default=False)
    tcp_connection_count = db.Column(db.Integer, nullable=True)
    udp_connection_count = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Info(name='{self.name}', ip='{self.ip}', browser='{self.browser}')"

    def __repr__(self):
        return f"Info(name='{self.name}', ip='{self.ip}', browser='{self.browser}')"