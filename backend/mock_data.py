# backend/mock_data.py

credit_cards = [
    {
        "id": "card1",
        "card_number": "**** **** **** 1234",
        "status": "active",
        "card_type": "Visa",
        "expiry": "12/25",
        "card_holder": "John Doe",
        "credit_limit": 50000,
        "available_credit": 3200
    },
    {
        "id": "card2",
        "card_number": "**** **** **** 5678",
        "status": "active",
        "card_type": "MasterCard",
        "expiry": "08/24",
        "card_holder": "John Doe",
        "credit_limit": 100000,
        "available_credit": 4500
    },
    {
        "id": "card3",
        "card_number": "**** **** **** 9876",
        "status": "active",
        "card_type": "Amex",
        "expiry": "03/26",
        "card_holder": "John Doe",
        "credit_limit": 150000,
        "available_credit": 12000
    }
]

transactions = [
    {
      "id": "txn1",
      "card_id": "card1",
      "date": "2024-05-01",
      "description": "Hotel Booking",
      "amount": 493.5,
      "category": "Food"
    },
    {
      "id": "txn2",
      "card_id": "card3",
      "date": "2024-01-04",
      "description": "Medical Bill",
      "amount": 509.62,
      "category": "Food"
    },
    {
      "id": "txn3",
      "card_id": "card1",
      "date": "2024-05-10",
      "description": "Restaurant Bill",
      "amount": 935.83,
      "category": "Food"
    },
    {
      "id": "txn4",
      "card_id": "card2",
      "date": "2024-04-20",
      "description": "Restaurant Bill",
      "amount": 1476.72,
      "category": "Utilities"
    },
    {
      "id": "txn5",
      "card_id": "card2",
      "date": "2024-01-24",
      "description": "App Store",
      "amount": 465.22,
      "category": "Shopping"
    },
    {
      "id": "txn6",
      "card_id": "card2",
      "date": "2024-01-09",
      "description": "Amazon Purchase",
      "amount": 225.17,
      "category": "Subscription"
    },
    {
      "id": "txn7",
      "card_id": "card2",
      "date": "2024-03-06",
      "description": "Grocery Store",
      "amount": 483.7,
      "category": "Transport"
    },
    {
      "id": "txn8",
      "card_id": "card2",
      "date": "2024-05-12",
      "description": "Hotel Booking",
      "amount": 1371.17,
      "category": "Health"
    },
    {
      "id": "txn9",
      "card_id": "card3",
      "date": "2024-01-24",
      "description": "Gym Membership",
      "amount": 657.42,
      "category": "Utilities"
    },
    {
      "id": "txn10",
      "card_id": "card2",
      "date": "2024-02-17",
      "description": "Movie Tickets",
      "amount": 245.64,
      "category": "Subscription"
    },
    {
      "id": "txn11",
      "card_id": "card1",
      "date": "2024-04-09",
      "description": "Restaurant Bill",
      "amount": 322.66,
      "category": "Transport"
    },
    {
      "id": "txn12",
      "card_id": "card1",
      "date": "2024-03-22",
      "description": "App Store",
      "amount": 733.96,
      "category": "Shopping"
    },
    {
      "id": "txn13",
      "card_id": "card2",
      "date": "2024-02-01",
      "description": "Electricity Bill",
      "amount": 413.86,
      "category": "Utilities"
    },
    {
      "id": "txn14",
      "card_id": "card1",
      "date": "2024-02-10",
      "description": "Uber Ride",
      "amount": 436.69,
      "category": "Food"
    },
    {
      "id": "txn15",
      "card_id": "card1",
      "date": "2024-03-29",
      "description": "Amazon Purchase",
      "amount": 442.45,
      "category": "Utilities"
    },
    {
      "id": "txn16",
      "card_id": "card2",
      "date": "2024-02-09",
      "description": "Grocery Store",
      "amount": 1420.44,
      "category": "Utilities"
    },
    {
      "id": "txn17",
      "card_id": "card2",
      "date": "2024-02-27",
      "description": "Hotel Booking",
      "amount": 742.49,
      "category": "Entertainment"
    },
    {
      "id": "txn18",
      "card_id": "card2",
      "date": "2024-02-20",
      "description": "Electricity Bill",
      "amount": 515.96,
      "category": "Transport"
    },
    {
      "id": "txn19",
      "card_id": "card2",
      "date": "2024-02-21",
      "description": "App Store",
      "amount": 583.77,
      "category": "Health"
    },
    {
      "id": "txn20",
      "card_id": "card2",
      "date": "2024-03-24",
      "description": "Gym Membership",
      "amount": 1444.2,
      "category": "Subscription"
    },
    {
      "id": "txn21",
      "card_id": "card1",
      "date": "2024-04-06",
      "description": "Grocery Store",
      "amount": 47.3,
      "category": "Entertainment"
    },
    {
      "id": "txn22",
      "card_id": "card1",
      "date": "2024-01-06",
      "description": "Amazon Purchase",
      "amount": 1017.43,
      "category": "Food"
    },
    {
      "id": "txn23",
      "card_id": "card2",
      "date": "2024-03-08",
      "description": "Netflix Subscription",
      "amount": 1314.55,
      "category": "Shopping"
    },
    {
      "id": "txn24",
      "card_id": "card1",
      "date": "2024-05-25",
      "description": "Uber Ride",
      "amount": 177.19,
      "category": "Food"
    },
    {
      "id": "txn25",
      "card_id": "card2",
      "date": "2024-05-08",
      "description": "Amazon Purchase",
      "amount": 999.64,
      "category": "Travel"
    },
    {
      "id": "txn26",
      "card_id": "card1",
      "date": "2024-05-04",
      "description": "Electricity Bill",
      "amount": 1080.38,
      "category": "Transport"
    },
    {
      "id": "txn27",
      "card_id": "card3",
      "date": "2024-04-06",
      "description": "Grocery Store",
      "amount": 512.39,
      "category": "Food"
    },
    {
      "id": "txn28",
      "card_id": "card1",
      "date": "2024-03-03",
      "description": "Grocery Store",
      "amount": 513.61,
      "category": "Travel"
    },
    {
      "id": "txn29",
      "card_id": "card2",
      "date": "2024-03-01",
      "description": "App Store",
      "amount": 299.9,
      "category": "Travel"
    },
    {
      "id": "txn30",
      "card_id": "card2",
      "date": "2024-01-27",
      "description": "App Store",
      "amount": 931.68,
      "category": "Travel"
    },
    {
      "id": "txn31",
      "card_id": "card2",
      "date": "2024-03-12",
      "description": "Airline Ticket",
      "amount": 435.05,
      "category": "Health"
    },
    {
      "id": "txn32",
      "card_id": "card3",
      "date": "2024-01-21",
      "description": "Gym Membership",
      "amount": 352.35,
      "category": "Transport"
    },
    {
      "id": "txn33",
      "card_id": "card1",
      "date": "2024-05-09",
      "description": "App Store",
      "amount": 947.77,
      "category": "Entertainment"
    },
    {
      "id": "txn34",
      "card_id": "card1",
      "date": "2024-01-20",
      "description": "Gym Membership",
      "amount": 1017.59,
      "category": "Utilities"
    },
    {
      "id": "txn35",
      "card_id": "card1",
      "date": "2024-01-19",
      "description": "Electricity Bill",
      "amount": 653.05,
      "category": "Health"
    },
    {
      "id": "txn36",
      "card_id": "card3",
      "date": "2024-04-01",
      "description": "Netflix Subscription",
      "amount": 759.37,
      "category": "Health"
    },
    {
      "id": "txn37",
      "card_id": "card2",
      "date": "2024-03-14",
      "description": "Uber Ride",
      "amount": 995.01,
      "category": "Shopping"
    },
    {
      "id": "txn38",
      "card_id": "card3",
      "date": "2024-05-08",
      "description": "App Store",
      "amount": 389.82,
      "category": "Entertainment"
    },
    {
      "id": "txn39",
      "card_id": "card2",
      "date": "2024-01-09",
      "description": "Airline Ticket",
      "amount": 723.39,
      "category": "Subscription"
    },
    {
      "id": "txn40",
      "card_id": "card1",
      "date": "2024-01-19",
      "description": "App Store",
      "amount": 609.49,
      "category": "Food"
    },
    {
      "id": "txn41",
      "card_id": "card1",
      "date": "2024-04-22",
      "description": "Airline Ticket",
      "amount": 1062.43,
      "category": "Travel"
    },
    {
      "id": "txn42",
      "card_id": "card1",
      "date": "2024-06-07",
      "description": "App Store",
      "amount": 858.45,
      "category": "Subscription"
    },
    {
      "id": "txn43",
      "card_id": "card1",
      "date": "2024-01-11",
      "description": "Uber Ride",
      "amount": 284.68,
      "category": "Travel"
    },
    {
      "id": "txn44",
      "card_id": "card3",
      "date": "2024-04-11",
      "description": "Gym Membership",
      "amount": 430.77,
      "category": "Subscription"
    },
    {
      "id": "txn45",
      "card_id": "card3",
      "date": "2024-03-05",
      "description": "Airline Ticket",
      "amount": 51.0,
      "category": "Transport"
    },
    {
      "id": "txn46",
      "card_id": "card3",
      "date": "2024-06-09",
      "description": "App Store",
      "amount": 158.78,
      "category": "Entertainment"
    },
    {
      "id": "txn47",
      "card_id": "card1",
      "date": "2024-03-09",
      "description": "Uber Ride",
      "amount": 27.86,
      "category": "Subscription"
    },
    {
      "id": "txn48",
      "card_id": "card1",
      "date": "2024-05-12",
      "description": "Grocery Store",
      "amount": 184.18,
      "category": "Transport"
    },
    {
      "id": "txn49",
      "card_id": "card1",
      "date": "2024-01-25",
      "description": "Amazon Purchase",
      "amount": 925.4,
      "category": "Entertainment"
    },
    {
      "id": "txn50",
      "card_id": "card1",
      "date": "2024-02-20",
      "description": "Medical Bill",
      "amount": 930.96,
      "category": "Health"
    },
    {
      "id": "txn51",
      "card_id": "card1",
      "date": "2024-02-04",
      "description": "App Store",
      "amount": 449.81,
      "category": "Shopping"
    },
    {
      "id": "txn52",
      "card_id": "card2",
      "date": "2024-01-03",
      "description": "Airline Ticket",
      "amount": 923.82,
      "category": "Subscription"
    },
    {
      "id": "txn53",
      "card_id": "card3",
      "date": "2024-04-01",
      "description": "Medical Bill",
      "amount": 1011.77,
      "category": "Food"
    },
    {
      "id": "txn54",
      "card_id": "card2",
      "date": "2024-01-10",
      "description": "Movie Tickets",
      "amount": 1035.33,
      "category": "Utilities"
    },
    {
      "id": "txn55",
      "card_id": "card1",
      "date": "2024-05-21",
      "description": "Grocery Store",
      "amount": 482.86,
      "category": "Travel"
    },
    {
      "id": "txn56",
      "card_id": "card1",
      "date": "2024-06-03",
      "description": "App Store",
      "amount": 670.86,
      "category": "Utilities"
    },
    {
      "id": "txn57",
      "card_id": "card3",
      "date": "2024-03-22",
      "description": "Medical Bill",
      "amount": 1414.47,
      "category": "Entertainment"
    },
    {
      "id": "txn58",
      "card_id": "card1",
      "date": "2024-02-20",
      "description": "Movie Tickets",
      "amount": 1286.84,
      "category": "Food"
    },
    {
      "id": "txn59",
      "card_id": "card1",
      "date": "2024-05-04",
      "description": "Grocery Store",
      "amount": 116.34,
      "category": "Entertainment"
    },
    {
      "id": "txn60",
      "card_id": "card1",
      "date": "2024-03-11",
      "description": "Restaurant Bill",
      "amount": 828.05,
      "category": "Subscription"
    },
    {
      "id": "txn61",
      "card_id": "card1",
      "date": "2024-05-26",
      "description": "Movie Tickets",
      "amount": 1206.91,
      "category": "Health"
    },
    {
      "id": "txn62",
      "card_id": "card1",
      "date": "2024-02-06",
      "description": "Grocery Store",
      "amount": 925.71,
      "category": "Utilities"
    },
    {
      "id": "txn63",
      "card_id": "card3",
      "date": "2024-06-08",
      "description": "Electricity Bill",
      "amount": 89.54,
      "category": "Shopping"
    },
    {
      "id": "txn64",
      "card_id": "card2",
      "date": "2024-01-06",
      "description": "Airline Ticket",
      "amount": 1077.21,
      "category": "Shopping"
    },
    {
      "id": "txn65",
      "card_id": "card2",
      "date": "2024-03-18",
      "description": "Electricity Bill",
      "amount": 698.65,
      "category": "Utilities"
    },
    {
      "id": "txn66",
      "card_id": "card2",
      "date": "2024-03-27",
      "description": "Netflix Subscription",
      "amount": 954.52,
      "category": "Entertainment"
    },
    {
      "id": "txn67",
      "card_id": "card2",
      "date": "2024-01-13",
      "description": "Grocery Store",
      "amount": 18.82,
      "category": "Shopping"
    },
    {
      "id": "txn68",
      "card_id": "card2",
      "date": "2024-01-06",
      "description": "App Store",
      "amount": 1457.95,
      "category": "Transport"
    },
    {
      "id": "txn69",
      "card_id": "card1",
      "date": "2024-05-15",
      "description": "App Store",
      "amount": 512.13,
      "category": "Shopping"
    },
    {
      "id": "txn70",
      "card_id": "card1",
      "date": "2024-04-04",
      "description": "Amazon Purchase",
      "amount": 666.51,
      "category": "Food"
    },
    {
      "id": "txn71",
      "card_id": "card3",
      "date": "2024-03-27",
      "description": "Airline Ticket",
      "amount": 1427.79,
      "category": "Utilities"
    },
    {
      "id": "txn72",
      "card_id": "card1",
      "date": "2024-05-24",
      "description": "Airline Ticket",
      "amount": 536.91,
      "category": "Food"
    },
    {
      "id": "txn73",
      "card_id": "card3",
      "date": "2024-04-12",
      "description": "Medical Bill",
      "amount": 1054.46,
      "category": "Transport"
    },
    {
      "id": "txn74",
      "card_id": "card3",
      "date": "2024-05-09",
      "description": "Medical Bill",
      "amount": 350.9,
      "category": "Travel"
    },
    {
      "id": "txn75",
      "card_id": "card1",
      "date": "2024-01-06",
      "description": "Grocery Store",
      "amount": 1103.69,
      "category": "Shopping"
    },
    {
      "id": "txn76",
      "card_id": "card1",
      "date": "2024-03-01",
      "description": "Airline Ticket",
      "amount": 1413.15,
      "category": "Travel"
    },
    {
      "id": "txn77",
      "card_id": "card2",
      "date": "2024-03-28",
      "description": "Gym Membership",
      "amount": 268.91,
      "category": "Entertainment"
    },
    {
      "id": "txn78",
      "card_id": "card1",
      "date": "2024-02-01",
      "description": "Uber Ride",
      "amount": 124.65,
      "category": "Travel"
    },
    {
      "id": "txn79",
      "card_id": "card3",
      "date": "2024-04-09",
      "description": "Restaurant Bill",
      "amount": 10.34,
      "category": "Health"
    },
    {
      "id": "txn80",
      "card_id": "card2",
      "date": "2024-04-15",
      "description": "Uber Ride",
      "amount": 10.13,
      "category": "Health"
    },
    {
      "id": "txn81",
      "card_id": "card1",
      "date": "2024-04-17",
      "description": "App Store",
      "amount": 1176.03,
      "category": "Shopping"
    },
    {
      "id": "txn82",
      "card_id": "card3",
      "date": "2024-02-17",
      "description": "Restaurant Bill",
      "amount": 399.07,
      "category": "Shopping"
    },
    {
      "id": "txn83",
      "card_id": "card1",
      "date": "2024-01-14",
      "description": "Netflix Subscription",
      "amount": 849.95,
      "category": "Entertainment"
    },
    {
      "id": "txn84",
      "card_id": "card2",
      "date": "2024-04-13",
      "description": "Movie Tickets",
      "amount": 1303.46,
      "category": "Transport"
    },
    {
      "id": "txn85",
      "card_id": "card3",
      "date": "2024-03-06",
      "description": "Uber Ride",
      "amount": 69.27,
      "category": "Health"
    },
    {
      "id": "txn86",
      "card_id": "card3",
      "date": "2024-01-20",
      "description": "Electricity Bill",
      "amount": 475.1,
      "category": "Food"
    },
    {
      "id": "txn87",
      "card_id": "card2",
      "date": "2024-02-15",
      "description": "Gym Membership",
      "amount": 985.86,
      "category": "Entertainment"
    },
    {
      "id": "txn88",
      "card_id": "card3",
      "date": "2024-04-08",
      "description": "Movie Tickets",
      "amount": 582.93,
      "category": "Food"
    },
    {
      "id": "txn89",
      "card_id": "card1",
      "date": "2024-03-27",
      "description": "Hotel Booking",
      "amount": 972.45,
      "category": "Health"
    },
    {
      "id": "txn90",
      "card_id": "card1",
      "date": "2024-05-28",
      "description": "Uber Ride",
      "amount": 487.53,
      "category": "Health"
    },
    {
      "id": "txn91",
      "card_id": "card1",
      "date": "2024-05-11",
      "description": "Grocery Store",
      "amount": 273.49,
      "category": "Travel"
    },
    {
      "id": "txn92",
      "card_id": "card2",
      "date": "2024-01-31",
      "description": "Uber Ride",
      "amount": 608.44,
      "category": "Health"
    },
    {
      "id": "txn93",
      "card_id": "card2",
      "date": "2024-05-13",
      "description": "Amazon Purchase",
      "amount": 1148.48,
      "category": "Transport"
    },
    {
      "id": "txn94",
      "card_id": "card1",
      "date": "2024-03-14",
      "description": "Movie Tickets",
      "amount": 61.28,
      "category": "Travel"
    },
    {
      "id": "txn95",
      "card_id": "card2",
      "date": "2024-02-17",
      "description": "Netflix Subscription",
      "amount": 589.89,
      "category": "Food"
    },
    {
      "id": "txn96",
      "card_id": "card1",
      "date": "2024-04-16",
      "description": "Netflix Subscription",
      "amount": 1160.55,
      "category": "Shopping"
    },
    {
      "id": "txn97",
      "card_id": "card2",
      "date": "2024-01-23",
      "description": "Uber Ride",
      "amount": 591.93,
      "category": "Subscription"
    },
    {
      "id": "txn98",
      "card_id": "card1",
      "date": "2024-01-10",
      "description": "Restaurant Bill",
      "amount": 1269.57,
      "category": "Health"
    },
    {
      "id": "txn99",
      "card_id": "card1",
      "date": "2024-03-22",
      "description": "Grocery Store",
      "amount": 1319.62,
      "category": "Subscription"
    },
    {
      "id": "txn100",
      "card_id": "card2",
      "date": "2024-02-29",
      "description": "Movie Tickets",
      "amount": 210.9,
      "category": "Health"
    },
    {
      "id": "txn101",
      "card_id": "card2",
      "date": "2024-02-09",
      "description": "Uber Ride",
      "amount": 1230.1,
      "category": "Transport"
    },
    {
      "id": "txn102",
      "card_id": "card3",
      "date": "2024-02-25",
      "description": "Grocery Store",
      "amount": 1136.32,
      "category": "Transport"
    },
    {
      "id": "txn103",
      "card_id": "card2",
      "date": "2024-02-10",
      "description": "Uber Ride",
      "amount": 991.84,
      "category": "Subscription"
    },
    {
      "id": "txn104",
      "card_id": "card2",
      "date": "2024-03-26",
      "description": "Airline Ticket",
      "amount": 946.73,
      "category": "Utilities"
    },
    {
      "id": "txn105",
      "card_id": "card1",
      "date": "2024-05-26",
      "description": "Grocery Store",
      "amount": 578.93,
      "category": "Health"
    },
    {
      "id": "txn106",
      "card_id": "card2",
      "date": "2024-01-31",
      "description": "Uber Ride",
      "amount": 779.22,
      "category": "Shopping"
    },
    {
      "id": "txn107",
      "card_id": "card3",
      "date": "2024-05-29",
      "description": "Amazon Purchase",
      "amount": 1131.64,
      "category": "Health"
    },
    {
      "id": "txn108",
      "card_id": "card2",
      "date": "2024-04-12",
      "description": "Hotel Booking",
      "amount": 1250.71,
      "category": "Shopping"
    },
    {
      "id": "txn109",
      "card_id": "card3",
      "date": "2024-03-12",
      "description": "Restaurant Bill",
      "amount": 346.39,
      "category": "Health"
    },
    {
      "id": "txn110",
      "card_id": "card2",
      "date": "2024-01-09",
      "description": "Gym Membership",
      "amount": 699.9,
      "category": "Transport"
    },
    {
      "id": "txn111",
      "card_id": "card1",
      "date": "2024-03-27",
      "description": "Medical Bill",
      "amount": 1292.18,
      "category": "Entertainment"
    },
    {
      "id": "txn112",
      "card_id": "card2",
      "date": "2024-05-14",
      "description": "App Store",
      "amount": 81.6,
      "category": "Health"
    },
    {
      "id": "txn113",
      "card_id": "card3",
      "date": "2024-04-26",
      "description": "Amazon Purchase",
      "amount": 1477.76,
      "category": "Food"
    },
    {
      "id": "txn114",
      "card_id": "card2",
      "date": "2024-05-15",
      "description": "Gym Membership",
      "amount": 1327.64,
      "category": "Subscription"
    },
    {
      "id": "txn115",
      "card_id": "card1",
      "date": "2024-04-17",
      "description": "Gym Membership",
      "amount": 928.77,
      "category": "Shopping"
    },
    {
      "id": "txn116",
      "card_id": "card3",
      "date": "2024-01-21",
      "description": "Uber Ride",
      "amount": 775.81,
      "category": "Health"
    },
    {
      "id": "txn117",
      "card_id": "card2",
      "date": "2024-05-21",
      "description": "Amazon Purchase",
      "amount": 1234.82,
      "category": "Food"
    },
    {
      "id": "txn118",
      "card_id": "card2",
      "date": "2024-02-03",
      "description": "Airline Ticket",
      "amount": 435.29,
      "category": "Shopping"
    },
    {
      "id": "txn119",
      "card_id": "card1",
      "date": "2024-06-08",
      "description": "Amazon Purchase",
      "amount": 466.13,
      "category": "Utilities"
    },
    {
      "id": "txn120",
      "card_id": "card1",
      "date": "2024-03-05",
      "description": "Grocery Store",
      "amount": 1187.15,
      "category": "Entertainment"
    },
    {
      "id": "txn121",
      "card_id": "card3",
      "date": "2024-04-18",
      "description": "Movie Tickets",
      "amount": 309.37,
      "category": "Subscription"
    },
    {
      "id": "txn122",
      "card_id": "card3",
      "date": "2024-01-24",
      "description": "Restaurant Bill",
      "amount": 1207.89,
      "category": "Entertainment"
    },
    {
      "id": "txn123",
      "card_id": "card1",
      "date": "2024-05-02",
      "description": "Gym Membership",
      "amount": 463.92,
      "category": "Entertainment"
    },
    {
      "id": "txn124",
      "card_id": "card2",
      "date": "2024-02-21",
      "description": "Hotel Booking",
      "amount": 793.79,
      "category": "Shopping"
    },
    {
      "id": "txn125",
      "card_id": "card3",
      "date": "2024-05-20",
      "description": "Amazon Purchase",
      "amount": 299.36,
      "category": "Utilities"
    },
    {
      "id": "txn126",
      "card_id": "card3",
      "date": "2024-06-02",
      "description": "Amazon Purchase",
      "amount": 951.83,
      "category": "Travel"
    },
    {
      "id": "txn127",
      "card_id": "card1",
      "date": "2024-04-21",
      "description": "Movie Tickets",
      "amount": 402.93,
      "category": "Health"
    },
    {
      "id": "txn128",
      "card_id": "card2",
      "date": "2024-04-27",
      "description": "Airline Ticket",
      "amount": 902.01,
      "category": "Subscription"
    },
    {
      "id": "txn129",
      "card_id": "card2",
      "date": "2024-01-12",
      "description": "Electricity Bill",
      "amount": 171.99,
      "category": "Transport"
    },
    {
      "id": "txn130",
      "card_id": "card1",
      "date": "2024-03-30",
      "description": "Medical Bill",
      "amount": 1407.99,
      "category": "Entertainment"
    },
    {
      "id": "txn131",
      "card_id": "card3",
      "date": "2024-04-28",
      "description": "Airline Ticket",
      "amount": 1466.0,
      "category": "Travel"
    },
    {
      "id": "txn132",
      "card_id": "card3",
      "date": "2024-01-27",
      "description": "Restaurant Bill",
      "amount": 872.38,
      "category": "Travel"
    },
    {
      "id": "txn133",
      "card_id": "card1",
      "date": "2024-06-02",
      "description": "Gym Membership",
      "amount": 1276.78,
      "category": "Health"
    },
    {
      "id": "txn134",
      "card_id": "card2",
      "date": "2024-04-25",
      "description": "Netflix Subscription",
      "amount": 434.84,
      "category": "Entertainment"
    },
    {
      "id": "txn135",
      "card_id": "card2",
      "date": "2024-02-03",
      "description": "Electricity Bill",
      "amount": 37.72,
      "category": "Food"
    },
    {
      "id": "txn136",
      "card_id": "card1",
      "date": "2024-01-25",
      "description": "Netflix Subscription",
      "amount": 1224.99,
      "category": "Food"
    },
    {
      "id": "txn137",
      "card_id": "card3",
      "date": "2024-05-28",
      "description": "App Store",
      "amount": 822.59,
      "category": "Utilities"
    },
    {
      "id": "txn138",
      "card_id": "card3",
      "date": "2024-02-07",
      "description": "Amazon Purchase",
      "amount": 1063.85,
      "category": "Transport"
    },
    {
      "id": "txn139",
      "card_id": "card3",
      "date": "2024-03-15",
      "description": "Electricity Bill",
      "amount": 817.24,
      "category": "Subscription"
    },
    {
      "id": "txn140",
      "card_id": "card1",
      "date": "2024-03-29",
      "description": "Airline Ticket",
      "amount": 1162.47,
      "category": "Health"
    },
    {
      "id": "txn141",
      "card_id": "card2",
      "date": "2024-03-07",
      "description": "Hotel Booking",
      "amount": 1079.74,
      "category": "Transport"
    },
    {
      "id": "txn142",
      "card_id": "card1",
      "date": "2024-02-02",
      "description": "Medical Bill",
      "amount": 497.41,
      "category": "Shopping"
    },
    {
      "id": "txn143",
      "card_id": "card1",
      "date": "2024-03-21",
      "description": "Restaurant Bill",
      "amount": 1391.01,
      "category": "Travel"
    },
    {
      "id": "txn144",
      "card_id": "card3",
      "date": "2024-05-29",
      "description": "Airline Ticket",
      "amount": 189.67,
      "category": "Utilities"
    },
    {
      "id": "txn145",
      "card_id": "card2",
      "date": "2024-06-09",
      "description": "Restaurant Bill",
      "amount": 527.72,
      "category": "Food"
    },
    {
      "id": "txn146",
      "card_id": "card3",
      "date": "2024-04-28",
      "description": "Hotel Booking",
      "amount": 1236.3,
      "category": "Health"
    },
    {
      "id": "txn147",
      "card_id": "card3",
      "date": "2024-05-31",
      "description": "Restaurant Bill",
      "amount": 287.37,
      "category": "Entertainment"
    },
    {
      "id": "txn148",
      "card_id": "card3",
      "date": "2024-01-12",
      "description": "Grocery Store",
      "amount": 524.43,
      "category": "Entertainment"
    },
    {
      "id": "txn149",
      "card_id": "card3",
      "date": "2024-03-10",
      "description": "Amazon Purchase",
      "amount": 1358.3,
      "category": "Shopping"
    },
    {
      "id": "txn150",
      "card_id": "card3",
      "date": "2024-01-31",
      "description": "Hotel Booking",
      "amount": 387.42,
      "category": "Travel"
    },
    {
      "id": "txn151",
      "card_id": "card1",
      "date": "2024-03-26",
      "description": "Gym Membership",
      "amount": 950.28,
      "category": "Food"
    },
    {
      "id": "txn152",
      "card_id": "card3",
      "date": "2024-05-26",
      "description": "App Store",
      "amount": 29.92,
      "category": "Transport"
    },
    {
      "id": "txn153",
      "card_id": "card1",
      "date": "2024-05-25",
      "description": "Amazon Purchase",
      "amount": 536.96,
      "category": "Transport"
    },
    {
      "id": "txn154",
      "card_id": "card1",
      "date": "2024-02-29",
      "description": "Amazon Purchase",
      "amount": 171.65,
      "category": "Utilities"
    },
    {
      "id": "txn155",
      "card_id": "card2",
      "date": "2024-05-20",
      "description": "Restaurant Bill",
      "amount": 823.1,
      "category": "Travel"
    },
    {
      "id": "txn156",
      "card_id": "card2",
      "date": "2024-02-17",
      "description": "Airline Ticket",
      "amount": 421.34,
      "category": "Subscription"
    },
    {
      "id": "txn157",
      "card_id": "card2",
      "date": "2024-06-02",
      "description": "App Store",
      "amount": 1021.19,
      "category": "Shopping"
    },
    {
      "id": "txn158",
      "card_id": "card1",
      "date": "2024-04-19",
      "description": "Restaurant Bill",
      "amount": 148.34,
      "category": "Health"
    },
    {
      "id": "txn159",
      "card_id": "card1",
      "date": "2024-02-09",
      "description": "App Store",
      "amount": 272.92,
      "category": "Travel"
    },
    {
      "id": "txn160",
      "card_id": "card2",
      "date": "2024-04-12",
      "description": "Movie Tickets",
      "amount": 461.31,
      "category": "Transport"
    },
    {
      "id": "txn161",
      "card_id": "card3",
      "date": "2024-02-10",
      "description": "App Store",
      "amount": 444.47,
      "category": "Health"
    },
    {
      "id": "txn162",
      "card_id": "card1",
      "date": "2024-04-05",
      "description": "App Store",
      "amount": 1385.7,
      "category": "Utilities"
    },
    {
      "id": "txn163",
      "card_id": "card3",
      "date": "2024-01-05",
      "description": "Movie Tickets",
      "amount": 1050.27,
      "category": "Travel"
    },
    {
      "id": "txn164",
      "card_id": "card1",
      "date": "2024-06-04",
      "description": "Grocery Store",
      "amount": 215.01,
      "category": "Shopping"
    },
    {
      "id": "txn165",
      "card_id": "card2",
      "date": "2024-02-04",
      "description": "App Store",
      "amount": 543.88,
      "category": "Shopping"
    },
    {
      "id": "txn166",
      "card_id": "card2",
      "date": "2024-03-25",
      "description": "App Store",
      "amount": 975.07,
      "category": "Food"
    },
    {
      "id": "txn167",
      "card_id": "card3",
      "date": "2024-04-18",
      "description": "App Store",
      "amount": 362.05,
      "category": "Entertainment"
    },
    {
      "id": "txn168",
      "card_id": "card3",
      "date": "2024-02-12",
      "description": "Electricity Bill",
      "amount": 907.13,
      "category": "Subscription"
    },
    {
      "id": "txn169",
      "card_id": "card1",
      "date": "2024-02-13",
      "description": "Electricity Bill",
      "amount": 397.95,
      "category": "Subscription"
    },
    {
      "id": "txn170",
      "card_id": "card1",
      "date": "2024-02-10",
      "description": "Medical Bill",
      "amount": 78.16,
      "category": "Utilities"
    },
    {
      "id": "txn171",
      "card_id": "card2",
      "date": "2024-03-27",
      "description": "App Store",
      "amount": 1171.0,
      "category": "Health"
    },
    {
      "id": "txn172",
      "card_id": "card3",
      "date": "2024-04-25",
      "description": "Hotel Booking",
      "amount": 744.85,
      "category": "Entertainment"
    },
    {
      "id": "txn173",
      "card_id": "card2",
      "date": "2024-01-29",
      "description": "App Store",
      "amount": 873.96,
      "category": "Health"
    },
    {
      "id": "txn174",
      "card_id": "card3",
      "date": "2024-03-05",
      "description": "Netflix Subscription",
      "amount": 154.46,
      "category": "Shopping"
    },
    {
      "id": "txn175",
      "card_id": "card3",
      "date": "2024-04-13",
      "description": "Gym Membership",
      "amount": 929.61,
      "category": "Health"
    },
    {
      "id": "txn176",
      "card_id": "card3",
      "date": "2024-01-12",
      "description": "App Store",
      "amount": 1234.51,
      "category": "Transport"
    },
    {
      "id": "txn177",
      "card_id": "card3",
      "date": "2024-03-06",
      "description": "Movie Tickets",
      "amount": 177.94,
      "category": "Health"
    },
    {
      "id": "txn178",
      "card_id": "card3",
      "date": "2024-01-05",
      "description": "Amazon Purchase",
      "amount": 571.85,
      "category": "Travel"
    },
    {
      "id": "txn179",
      "card_id": "card1",
      "date": "2024-05-13",
      "description": "Gym Membership",
      "amount": 86.59,
      "category": "Shopping"
    },
    {
      "id": "txn180",
      "card_id": "card3",
      "date": "2024-05-12",
      "description": "Uber Ride",
      "amount": 1026.97,
      "category": "Subscription"
    },
    {
      "id": "txn181",
      "card_id": "card3",
      "date": "2024-02-05",
      "description": "Medical Bill",
      "amount": 605.02,
      "category": "Health"
    },
    {
      "id": "txn182",
      "card_id": "card1",
      "date": "2024-01-27",
      "description": "Restaurant Bill",
      "amount": 728.93,
      "category": "Entertainment"
    },
    {
      "id": "txn183",
      "card_id": "card1",
      "date": "2024-03-14",
      "description": "Movie Tickets",
      "amount": 221.98,
      "category": "Utilities"
    },
    {
      "id": "txn184",
      "card_id": "card3",
      "date": "2024-02-08",
      "description": "Electricity Bill",
      "amount": 1154.38,
      "category": "Food"
    },
    {
      "id": "txn185",
      "card_id": "card3",
      "date": "2024-04-18",
      "description": "Gym Membership",
      "amount": 1182.21,
      "category": "Food"
    },
    {
      "id": "txn186",
      "card_id": "card1",
      "date": "2024-03-26",
      "description": "Netflix Subscription",
      "amount": 1094.12,
      "category": "Food"
    },
    {
      "id": "txn187",
      "card_id": "card1",
      "date": "2024-04-01",
      "description": "Uber Ride",
      "amount": 1497.73,
      "category": "Food"
    },
    {
      "id": "txn188",
      "card_id": "card3",
      "date": "2024-05-25",
      "description": "Grocery Store",
      "amount": 958.52,
      "category": "Transport"
    },
    {
      "id": "txn189",
      "card_id": "card1",
      "date": "2024-05-10",
      "description": "Electricity Bill",
      "amount": 76.84,
      "category": "Utilities"
    },
    {
      "id": "txn190",
      "card_id": "card3",
      "date": "2024-04-10",
      "description": "Restaurant Bill",
      "amount": 660.15,
      "category": "Health"
    },
    {
      "id": "txn191",
      "card_id": "card3",
      "date": "2024-06-08",
      "description": "Hotel Booking",
      "amount": 1432.25,
      "category": "Transport"
    },
    {
      "id": "txn192",
      "card_id": "card2",
      "date": "2024-03-13",
      "description": "Restaurant Bill",
      "amount": 1016.04,
      "category": "Travel"
    },
    {
      "id": "txn193",
      "card_id": "card3",
      "date": "2024-02-15",
      "description": "Airline Ticket",
      "amount": 1106.22,
      "category": "Travel"
    },
    {
      "id": "txn194",
      "card_id": "card1",
      "date": "2024-01-24",
      "description": "Restaurant Bill",
      "amount": 260.46,
      "category": "Shopping"
    },
    {
      "id": "txn195",
      "card_id": "card1",
      "date": "2024-04-14",
      "description": "Airline Ticket",
      "amount": 336.21,
      "category": "Health"
    },
    {
      "id": "txn196",
      "card_id": "card2",
      "date": "2024-05-18",
      "description": "Grocery Store",
      "amount": 1316.08,
      "category": "Food"
    },
    {
      "id": "txn197",
      "card_id": "card2",
      "date": "2024-04-01",
      "description": "Restaurant Bill",
      "amount": 1315.38,
      "category": "Entertainment"
    },
    {
      "id": "txn198",
      "card_id": "card3",
      "date": "2024-04-14",
      "description": "Grocery Store",
      "amount": 1158.27,
      "category": "Travel"
    },
    {
      "id": "txn199",
      "card_id": "card2",
      "date": "2024-01-20",
      "description": "Gym Membership",
      "amount": 369.27,
      "category": "Health"
    },
    {
      "id": "txn200",
      "card_id": "card3",
      "date": "2024-04-22",
      "description": "Medical Bill",
      "amount": 1401.75,
      "category": "Food"
    },
    {
      "id": "txn201",
      "card_id": "card3",
      "date": "2024-04-19",
      "description": "Uber Ride",
      "amount": 478.3,
      "category": "Utilities"
    },
    {
      "id": "txn202",
      "card_id": "card2",
      "date": "2024-05-02",
      "description": "Electricity Bill",
      "amount": 774.01,
      "category": "Entertainment"
    },
    {
      "id": "txn203",
      "card_id": "card2",
      "date": "2024-01-08",
      "description": "Grocery Store",
      "amount": 649.96,
      "category": "Utilities"
    },
    {
      "id": "txn204",
      "card_id": "card2",
      "date": "2024-04-26",
      "description": "Grocery Store",
      "amount": 214.68,
      "category": "Subscription"
    },
    {
      "id": "txn205",
      "card_id": "card1",
      "date": "2024-01-04",
      "description": "Medical Bill",
      "amount": 23.82,
      "category": "Utilities"
    },
    {
      "id": "txn206",
      "card_id": "card1",
      "date": "2024-01-06",
      "description": "Electricity Bill",
      "amount": 975.65,
      "category": "Subscription"
    },
    {
      "id": "txn207",
      "card_id": "card3",
      "date": "2024-06-01",
      "description": "App Store",
      "amount": 1246.59,
      "category": "Food"
    },
    {
      "id": "txn208",
      "card_id": "card3",
      "date": "2024-04-21",
      "description": "Grocery Store",
      "amount": 659.26,
      "category": "Transport"
    },
    {
      "id": "txn209",
      "card_id": "card3",
      "date": "2024-01-30",
      "description": "Amazon Purchase",
      "amount": 177.87,
      "category": "Shopping"
    },
    {
      "id": "txn210",
      "card_id": "card2",
      "date": "2024-02-18",
      "description": "Uber Ride",
      "amount": 417.5,
      "category": "Utilities"
    },
    {
      "id": "txn211",
      "card_id": "card1",
      "date": "2024-02-27",
      "description": "Netflix Subscription",
      "amount": 789.88,
      "category": "Utilities"
    },
    {
      "id": "txn212",
      "card_id": "card3",
      "date": "2024-04-18",
      "description": "Restaurant Bill",
      "amount": 564.34,
      "category": "Transport"
    },
    {
      "id": "txn213",
      "card_id": "card3",
      "date": "2024-04-06",
      "description": "Amazon Purchase",
      "amount": 720.27,
      "category": "Utilities"
    },
    {
      "id": "txn214",
      "card_id": "card1",
      "date": "2024-01-22",
      "description": "Movie Tickets",
      "amount": 1302.54,
      "category": "Shopping"
    },
    {
      "id": "txn215",
      "card_id": "card3",
      "date": "2024-04-14",
      "description": "Hotel Booking",
      "amount": 276.22,
      "category": "Subscription"
    },
    {
      "id": "txn216",
      "card_id": "card1",
      "date": "2024-03-13",
      "description": "Medical Bill",
      "amount": 553.88,
      "category": "Utilities"
    },
    {
      "id": "txn217",
      "card_id": "card3",
      "date": "2024-06-07",
      "description": "Movie Tickets",
      "amount": 842.82,
      "category": "Shopping"
    },
    {
      "id": "txn218",
      "card_id": "card3",
      "date": "2024-01-04",
      "description": "Gym Membership",
      "amount": 1468.78,
      "category": "Entertainment"
    },
    {
      "id": "txn219",
      "card_id": "card1",
      "date": "2024-02-11",
      "description": "Gym Membership",
      "amount": 1397.96,
      "category": "Food"
    },
    {
      "id": "txn220",
      "card_id": "card1",
      "date": "2024-04-19",
      "description": "Grocery Store",
      "amount": 785.71,
      "category": "Travel"
    },
    {
      "id": "txn221",
      "card_id": "card3",
      "date": "2024-01-31",
      "description": "Airline Ticket",
      "amount": 818.83,
      "category": "Food"
    },
    {
      "id": "txn222",
      "card_id": "card1",
      "date": "2024-01-05",
      "description": "Restaurant Bill",
      "amount": 747.28,
      "category": "Subscription"
    },
    {
      "id": "txn223",
      "card_id": "card3",
      "date": "2024-05-07",
      "description": "Hotel Booking",
      "amount": 592.93,
      "category": "Shopping"
    },
    {
      "id": "txn224",
      "card_id": "card1",
      "date": "2024-05-17",
      "description": "Gym Membership",
      "amount": 353.66,
      "category": "Transport"
    },
    {
      "id": "txn225",
      "card_id": "card3",
      "date": "2024-02-27",
      "description": "Uber Ride",
      "amount": 101.65,
      "category": "Subscription"
    },
    {
      "id": "txn226",
      "card_id": "card3",
      "date": "2024-03-20",
      "description": "Amazon Purchase",
      "amount": 831.43,
      "category": "Transport"
    },
    {
      "id": "txn227",
      "card_id": "card3",
      "date": "2024-06-05",
      "description": "Restaurant Bill",
      "amount": 1269.04,
      "category": "Transport"
    },
    {
      "id": "txn228",
      "card_id": "card3",
      "date": "2024-05-27",
      "description": "Netflix Subscription",
      "amount": 846.59,
      "category": "Shopping"
    },
    {
      "id": "txn229",
      "card_id": "card3",
      "date": "2024-03-23",
      "description": "Airline Ticket",
      "amount": 834.75,
      "category": "Transport"
    },
    {
      "id": "txn230",
      "card_id": "card1",
      "date": "2024-03-17",
      "description": "Electricity Bill",
      "amount": 956.23,
      "category": "Entertainment"
    },
    {
      "id": "txn231",
      "card_id": "card2",
      "date": "2024-04-25",
      "description": "Restaurant Bill",
      "amount": 348.76,
      "category": "Shopping"
    },
    {
      "id": "txn232",
      "card_id": "card3",
      "date": "2024-02-16",
      "description": "Hotel Booking",
      "amount": 107.14,
      "category": "Food"
    },
    {
      "id": "txn233",
      "card_id": "card3",
      "date": "2024-02-08",
      "description": "Medical Bill",
      "amount": 466.66,
      "category": "Food"
    },
    {
      "id": "txn234",
      "card_id": "card2",
      "date": "2024-01-14",
      "description": "Grocery Store",
      "amount": 839.33,
      "category": "Shopping"
    },
    {
      "id": "txn235",
      "card_id": "card2",
      "date": "2024-03-27",
      "description": "Airline Ticket",
      "amount": 830.03,
      "category": "Travel"
    },
    {
      "id": "txn236",
      "card_id": "card2",
      "date": "2024-04-18",
      "description": "Electricity Bill",
      "amount": 581.52,
      "category": "Shopping"
    },
    {
      "id": "txn237",
      "card_id": "card3",
      "date": "2024-03-05",
      "description": "App Store",
      "amount": 758.23,
      "category": "Utilities"
    },
    {
      "id": "txn238",
      "card_id": "card2",
      "date": "2024-03-27",
      "description": "Airline Ticket",
      "amount": 449.51,
      "category": "Food"
    },
    {
      "id": "txn239",
      "card_id": "card1",
      "date": "2024-04-08",
      "description": "App Store",
      "amount": 1249.95,
      "category": "Subscription"
    },
    {
      "id": "txn240",
      "card_id": "card1",
      "date": "2024-03-29",
      "description": "Electricity Bill",
      "amount": 1149.34,
      "category": "Shopping"
    },
    {
      "id": "txn241",
      "card_id": "card2",
      "date": "2024-03-13",
      "description": "Airline Ticket",
      "amount": 1285.51,
      "category": "Subscription"
    },
    {
      "id": "txn242",
      "card_id": "card2",
      "date": "2024-01-17",
      "description": "Grocery Store",
      "amount": 911.16,
      "category": "Entertainment"
    },
    {
      "id": "txn243",
      "card_id": "card1",
      "date": "2024-05-20",
      "description": "Electricity Bill",
      "amount": 149.51,
      "category": "Transport"
    },
    {
      "id": "txn244",
      "card_id": "card2",
      "date": "2024-05-07",
      "description": "Movie Tickets",
      "amount": 967.28,
      "category": "Entertainment"
    },
    {
      "id": "txn245",
      "card_id": "card3",
      "date": "2024-03-17",
      "description": "Amazon Purchase",
      "amount": 1110.59,
      "category": "Entertainment"
    },
    {
      "id": "txn246",
      "card_id": "card3",
      "date": "2024-04-29",
      "description": "Medical Bill",
      "amount": 942.05,
      "category": "Shopping"
    },
    {
      "id": "txn247",
      "card_id": "card1",
      "date": "2024-05-03",
      "description": "Gym Membership",
      "amount": 345.35,
      "category": "Subscription"
    },
    {
      "id": "txn248",
      "card_id": "card2",
      "date": "2024-04-09",
      "description": "Amazon Purchase",
      "amount": 1027.3,
      "category": "Subscription"
    },
    {
      "id": "txn249",
      "card_id": "card3",
      "date": "2024-05-24",
      "description": "Electricity Bill",
      "amount": 761.81,
      "category": "Health"
    },
    {
      "id": "txn250",
      "card_id": "card1",
      "date": "2024-06-02",
      "description": "Restaurant Bill",
      "amount": 771.87,
      "category": "Travel"
    }
  ]