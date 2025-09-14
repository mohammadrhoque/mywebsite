#!/usr/bin/env python3
"""
Create properly indexed SQLite database for sql.js-httpvfs
This script creates a comprehensive database with proper indexing for efficient queries
"""

import sqlite3
import json
import os

def create_indexed_bangladesh_database():
    """Create SQLite database with proper indexing for sql.js-httpvfs"""
    
    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect('bangladesh_map.db')
    cursor = conn.cursor()
    
    # Create divisions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS divisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_bengali TEXT,
            capital TEXT,
            area_km2 REAL,
            population INTEGER,
            established_year INTEGER,
            coordinates TEXT,
            description TEXT
        )
    ''')
    
    # Create districts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS districts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_bengali TEXT,
            division_id INTEGER,
            area_km2 REAL,
            population INTEGER,
            coordinates TEXT,
            upazilas_count INTEGER,
            FOREIGN KEY (division_id) REFERENCES divisions (id)
        )
    ''')
    
    # Create upazilas table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS upazilas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_bengali TEXT,
            district_id INTEGER,
            area_km2 REAL,
            population INTEGER,
            coordinates TEXT,
            union_count INTEGER,
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Create rivers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_bengali TEXT,
            length_km REAL,
            source TEXT,
            mouth TEXT,
            coordinates TEXT,
            description TEXT
        )
    ''')
    
    # Create landmarks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_bengali TEXT,
            type TEXT,
            division_id INTEGER,
            district_id INTEGER,
            coordinates TEXT,
            description TEXT,
            established_year INTEGER,
            FOREIGN KEY (division_id) REFERENCES divisions (id),
            FOREIGN KEY (district_id) REFERENCES districts (id)
        )
    ''')
    
    # Insert divisions data
    divisions_data = [
        ('Dhaka', 'ঢাকা', 'Dhaka', 31119.0, 44000000, 1971, 
         json.dumps({"lat": 23.8103, "lng": 90.4125}), 
         'Capital division and most populous region'),
        ('Chittagong', 'চট্টগ্রাম', 'Chittagong', 33908.0, 28000000, 1971,
         json.dumps({"lat": 22.3569, "lng": 91.7832}),
         'Major port city and industrial hub'),
        ('Rajshahi', 'রাজশাহী', 'Rajshahi', 18174.0, 18000000, 1971,
         json.dumps({"lat": 24.3745, "lng": 88.6042}),
         'Agricultural region in the northwest'),
        ('Khulna', 'খুলনা', 'Khulna', 22284.0, 15000000, 1971,
         json.dumps({"lat": 22.8456, "lng": 89.5403}),
         'Southwestern region with mangrove forests'),
        ('Barisal', 'বরিশাল', 'Barisal', 13297.0, 8000000, 1971,
         json.dumps({"lat": 22.7010, "lng": 90.3535}),
         'Riverine region in the south'),
        ('Sylhet', 'সিলেট', 'Sylhet', 12595.0, 9000000, 1971,
         json.dumps({"lat": 24.8949, "lng": 91.8687}),
         'Northeastern region with tea gardens'),
        ('Rangpur', 'রংপুর', 'Rangpur', 16317.0, 15000000, 2010,
         json.dumps({"lat": 25.7439, "lng": 89.2752}),
         'Northern region, newest division'),
        ('Mymensingh', 'ময়মনসিংহ', 'Mymensingh', 10584.0, 11000000, 2015,
         json.dumps({"lat": 24.7471, "lng": 90.4203}),
         'Central region, newest division')
    ]
    
    cursor.executemany('''
        INSERT INTO divisions (name, name_bengali, capital, area_km2, population, 
                             established_year, coordinates, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', divisions_data)
    
    # Insert districts data
    districts_data = [
        ('Dhaka', 'ঢাকা', 1, 1463.0, 12000000, 
         json.dumps({"lat": 23.8103, "lng": 90.4125}), 93),
        ('Chittagong', 'চট্টগ্রাম', 2, 5282.0, 8000000,
         json.dumps({"lat": 22.3569, "lng": 91.7832}), 11),
        ('Sylhet', 'সিলেট', 6, 3490.0, 3000000,
         json.dumps({"lat": 24.8949, "lng": 91.8687}), 13),
        ('Rajshahi', 'রাজশাহী', 3, 2407.0, 2500000,
         json.dumps({"lat": 24.3745, "lng": 88.6042}), 9),
        ('Khulna', 'খুলনা', 4, 4394.0, 2300000,
         json.dumps({"lat": 22.8456, "lng": 89.5403}), 9),
        ('Cox\'s Bazar', 'কক্সবাজার', 2, 2491.0, 2300000,
         json.dumps({"lat": 21.4272, "lng": 92.0058}), 8),
        ('Rangpur', 'রংপুর', 7, 2378.0, 2800000,
         json.dumps({"lat": 25.7439, "lng": 89.2752}), 8),
        ('Barisal', 'বরিশাল', 5, 2790.0, 2000000,
         json.dumps({"lat": 22.7010, "lng": 90.3535}), 6),
        ('Gazipur', 'গাজীপুর', 1, 1800.0, 3500000,
         json.dumps({"lat": 24.0023, "lng": 90.4264}), 5),
        ('Narayanganj', 'নারায়ণগঞ্জ', 1, 759.0, 3000000,
         json.dumps({"lat": 23.6238, "lng": 90.5000}), 5),
        ('Sylhet', 'সিলেট', 6, 3490.0, 3000000,
         json.dumps({"lat": 24.8949, "lng": 91.8687}), 13),
        ('Comilla', 'কুমিল্লা', 2, 3081.0, 5000000,
         json.dumps({"lat": 23.4607, "lng": 91.1809}), 16),
        ('Jessore', 'যশোর', 4, 2567.0, 2500000,
         json.dumps({"lat": 23.1707, "lng": 89.2098}), 8),
        ('Bogra', 'বগুড়া', 3, 2919.0, 3000000,
         json.dumps({"lat": 24.8510, "lng": 89.3695}), 12),
        ('Dinajpur', 'দিনাজপুর', 7, 3438.0, 3000000,
         json.dumps({"lat": 25.6273, "lng": 88.6331}), 13)
    ]
    
    cursor.executemany('''
        INSERT INTO districts (name, name_bengali, division_id, area_km2, 
                             population, coordinates, upazilas_count)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', districts_data)
    
    # Insert rivers data
    rivers_data = [
        ('Padma', 'পদ্মা', 120.0, 'Ganges River', 'Bay of Bengal',
         json.dumps([{"lat": 23.5, "lng": 89.0}, {"lat": 22.0, "lng": 90.0}]),
         'Main distributary of the Ganges'),
        ('Meghna', 'মেঘনা', 130.0, 'Barak River', 'Bay of Bengal',
         json.dumps([{"lat": 24.0, "lng": 91.0}, {"lat": 22.5, "lng": 90.5}]),
         'Major river in eastern Bangladesh'),
        ('Jamuna', 'যমুনা', 205.0, 'Brahmaputra River', 'Padma River',
         json.dumps([{"lat": 25.0, "lng": 89.5}, {"lat": 23.5, "lng": 89.0}]),
         'Main distributary of the Brahmaputra'),
        ('Karnaphuli', 'কর্ণফুলী', 180.0, 'Lushai Hills', 'Bay of Bengal',
         json.dumps([{"lat": 22.0, "lng": 92.0}, {"lat": 22.3, "lng": 91.8}]),
         'River flowing through Chittagong'),
        ('Surma', 'সুরমা', 245.0, 'Barak River', 'Meghna River',
         json.dumps([{"lat": 24.5, "lng": 92.0}, {"lat": 24.0, "lng": 91.0}]),
         'River in northeastern Bangladesh'),
        ('Teesta', 'তিস্তা', 315.0, 'Tso Lhamo Lake', 'Jamuna River',
         json.dumps([{"lat": 26.0, "lng": 88.5}, {"lat": 25.0, "lng": 89.5}]),
         'River in northern Bangladesh'),
        ('Brahmaputra', 'ব্রহ্মপুত্র', 2900.0, 'Angsi Glacier', 'Bay of Bengal',
         json.dumps([{"lat": 26.0, "lng": 88.0}, {"lat": 25.0, "lng": 89.0}]),
         'Major transboundary river'),
        ('Ganges', 'গঙ্গা', 2525.0, 'Gangotri Glacier', 'Bay of Bengal',
         json.dumps([{"lat": 24.0, "lng": 88.0}, {"lat": 23.0, "lng": 89.0}]),
         'Sacred river of India and Bangladesh')
    ]
    
    cursor.executemany('''
        INSERT INTO rivers (name, name_bengali, length_km, source, mouth, 
                          coordinates, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', rivers_data)
    
    # Insert landmarks data
    landmarks_data = [
        ('Sundarbans', 'সুন্দরবন', 'natural', 4, 5,
         json.dumps({"lat": 22.0, "lng": 89.0}),
         'Largest mangrove forest in the world', None),
        ('Cox\'s Bazar Beach', 'কক্সবাজার সমুদ্র সৈকত', 'natural', 2, 6,
         json.dumps({"lat": 21.4272, "lng": 92.0058}),
         'Longest natural sea beach in the world', None),
        ('Lalbagh Fort', 'লালবাগ কেল্লা', 'historical', 1, 1,
         json.dumps({"lat": 23.7193, "lng": 90.3881}),
         '17th-century Mughal fort in Dhaka', 1678),
        ('Shat Gombuj Mosque', 'ষাট গম্বুজ মসজিদ', 'historical', 4, 5,
         json.dumps({"lat": 22.6667, "lng": 89.7667}),
         '15th-century mosque in Bagerhat', 1459),
        ('Srimangal Tea Gardens', 'শ্রীমঙ্গল চা বাগান', 'cultural', 6, 3,
         json.dumps({"lat": 24.3, "lng": 91.7}),
         'Famous tea gardens in Sylhet', None),
        ('Paharpur Vihara', 'পাহাড়পুর বিহার', 'historical', 3, 4,
         json.dumps({"lat": 25.0333, "lng": 88.9833}),
         'Ancient Buddhist monastery', 8),
        ('Kuakata Beach', 'কুয়াকাটা সমুদ্র সৈকত', 'natural', 5, 8,
         json.dumps({"lat": 21.8167, "lng": 90.1167}),
         'Beach where you can see both sunrise and sunset', None),
        ('Ahsan Manzil', 'আহসান মঞ্জিল', 'historical', 1, 1,
         json.dumps({"lat": 23.7104, "lng": 90.4074}),
         'Pink Palace of Dhaka', 1872),
        ('National Parliament House', 'জাতীয় সংসদ ভবন', 'cultural', 1, 1,
         json.dumps({"lat": 23.7623, "lng": 90.3785}),
         'Modern architectural masterpiece', 1982),
        ('Chittagong Hill Tracts', 'চট্টগ্রাম পাহাড়ি অঞ্চল', 'natural', 2, 2,
         json.dumps({"lat": 22.5, "lng": 92.0}),
         'Mountainous region in southeastern Bangladesh', None)
    ]
    
    cursor.executemany('''
        INSERT INTO landmarks (name, name_bengali, type, division_id, district_id,
                             coordinates, description, established_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', landmarks_data)
    
    # Create comprehensive indexes for efficient queries
    print("Creating indexes for optimal performance...")
    
    # Primary indexes on frequently searched columns
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_name ON divisions(name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_name_bengali ON divisions(name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_capital ON divisions(capital)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_population ON divisions(population)')
    
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_name ON districts(name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_name_bengali ON districts(name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_division_id ON districts(division_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_population ON districts(population)')
    
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_name ON rivers(name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_name_bengali ON rivers(name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_length ON rivers(length_km)')
    
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_name ON landmarks(name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_name_bengali ON landmarks(name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_type ON landmarks(type)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_division_id ON landmarks(division_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_district_id ON landmarks(district_id)')
    
    # Composite indexes for complex queries
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_name_search ON divisions(name, name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_name_search ON districts(name, name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_name_search ON rivers(name, name_bengali)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_name_search ON landmarks(name, name_bengali)')
    
    # Text search indexes (for LIKE queries)
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_name_lower ON divisions(LOWER(name))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_divisions_bengali_lower ON divisions(LOWER(name_bengali))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_name_lower ON districts(LOWER(name))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_districts_bengali_lower ON districts(LOWER(name_bengali))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_name_lower ON rivers(LOWER(name))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rivers_bengali_lower ON rivers(LOWER(name_bengali))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_name_lower ON landmarks(LOWER(name))')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_landmarks_bengali_lower ON landmarks(LOWER(name_bengali))')
    
    # Analyze the database for query optimization
    cursor.execute('ANALYZE')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("✅ Indexed Bangladesh map database created successfully!")
    print("📊 Database contains:")
    print("   - 8 Divisions")
    print("   - 15 Major Districts")
    print("   - 8 Major Rivers")
    print("   - 10 Important Landmarks")
    print("🗄️ Database file: bangladesh_map.db")
    print("🔍 Optimized with comprehensive indexes for sql.js-httpvfs")

if __name__ == "__main__":
    create_indexed_bangladesh_database()
