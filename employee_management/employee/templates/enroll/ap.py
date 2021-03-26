data = {'id': 52,
        'address_line_1': 'malabar hill',
        'address_line_2': 'hanging garden',
        'city': 'mumbai', 'country': 'india',
        'pincode': '400006',
        'employees': [
            {
                'id': 34,
                'first_name': 'vishal',
                'last_name': 'syeda',
                'username': 'vishaladhav',
                'date_of_birth': '1997-08-09',
                'gender': 'M',
                'email_address': 'vshaladhav@gmail.com',
                'contact_number': 7977361393,
                'deleted': True}]}

data = {
    'id': 52,
    'address_line_1': 'malabar hill',
    'address_line_2': 'hanging garden',
    'city': 'mumbai', 'country': 'india',
    'pincode': '400006',
    "employees": [
        {
            'id': 34,
            'first_name': 'vishal',
            'last_name': 'syeda',
            'username': 'vishaladhav',
            'date_of_birth': '1997-08-09',
            'gender': 'M',
            'email_address': 'vshaladhav@gmail.com',
            'contact_number': 7977361393,
            'deleted': True
        }
    ]
}
data = {
    "id": 35,
    "first_name": "vsdsishal",
    "last_name": "adhav",
    "username": "vishaladhav",
    "date_of_birth": "1997-08-09",
    "gender": "M",
    "email_address": "vshaladhav@gmail.com",
    "contact_number": 7977361393,
    "deleted": True,
    "addressdetails": [
        {
            "id": 53,
            "address_line_1": "malabar hill",
            "address_line_2": "hanging garden",
            "city": "mumbai",
            "country": "india",
            "pincode": "400006",
        }
    ]
}


details = {
    "id": json_data["id"],
    "first_name": json_data["first_name"],
    "last_name": json_data["last_name"],
    "username": json_data["username"],
    "date_of_birth": json_data["date_of_birth"],
    "gender": json_data["gender"],
    "email_address": json_data["email_address"],
    "contact_number": json_data["contact_number"],
    "deleted": json_data["deleted"],
    "addressdetails": json_data[
        {
            "id": json_data["id"],
            "address_line_1": json_data["address_line_1"],
            "address_line_2": json_data["address_line_2"],
            "city": json_data["city"],
            "country": json_data["country"],
            "pincode": json_data["pincode"]
        }
    ]

}


#views

# def clients3(request):
#     return render(request, "enroll/showemp.html")


def save_data_test(self):
    details = {'address_line_1': 'masdlabar hill', 'address_line_2': 'hanginsdg garden', 'city': 'mumbai', 'country': 'india',
               'pincode': '400006',
               'employees': [{'first_name': 'vsdsishal', 'last_name': 'adhav', 'username': 'vishaladhav', 'date_of_birth': '1997-08-09', 'gender': 'M', 'email_address': 'vshaladhav@gmail.com', 'contact_number': 7977361393, 'deleted': True}]}

    music = AddressDetailsSerializer(data=details)
    print(music.is_valid())
    if music.is_valid():
        music.save()
        return HttpResponse("success")


def test_update(self):

    details = {
        'id': 52,
        'address_line_1': 'malabar hill',
        'address_line_2': 'hanging garden',
        'city': 'mumbai', 'country': 'india',
        'pincode': '400006',
        "employees": [
            {
                'id': 34,
                'first_name': 'vishal',
                'last_name': 'syeda',
                'username': 'vishaladhav',
                'date_of_birth': '1997-08-09',
                'gender': 'M',
                'email_address': 'vshaladhav@gmail.com',
                'contact_number': 7977361393,
                'deleted': True
            }
        ]
    }
    # val = AddressDetails.objects.get(id)
    music = AddressDetailsSerializer(val, data=details)
    print(music.is_valid())
    if music.is_valid():
        music.save()
        return HttpResponse("success")


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()



