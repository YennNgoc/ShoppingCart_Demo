import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?directConnection=true')

mydb=client['mongodb']


product_info = mydb['product']


list_products = [{
            	'product_id': 'P01',
	        'product_name': 'Chuột Logitech B100',
            	'product_type': {
		                    'product_type_code': 'T01',
		                    'parent_product_type_code': 'PT01',
		                    'product_type_description': 'chuột máy tính',
		                    },
                'product_info':{
                            'product_price': '80000',
	                        'product_color': 'đen',
	                        #'product_size': ,
	                        'product_description': 'Chuột có dây Logitech B100 Dây dài 1m8, thiết kế ôm tay, thuận cả 2 tay',
                },
	            'sale_person_id': 'S01',
                'promotion': {
                            'promotion_id': 'KM01',
                            'promotion_name': 'Giảm 5%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '5%',
                            }, 	
                },{
                'product_id': 'P02',
                'product_name': 'Chuột Chuột Razer Viper Ultimate',
                'product_type': {
                            'product_type_code': 'T01',
                            'parent_product_type_code': 'PT01',
                            'product_type_description': 'chuột máy tính',
                            },
                'product_info':{            
                            'product_price': '4000000',
                            'product_color': 'đen',
                            #'product_size': ,
                            'product_description': 'Chuột Razer Viper Ultimate không dây | Charging Dock',
                },
                'sale_person_id': 'S01',
                'promotion': {
                            'promotion_id': 'KM02',
                            'promotion_name': 'Giảm 10%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '10%',
                            }, 	
                },{
                'product_id': 'P03',
                'product_name': 'Chuột Logitech G304',
                'product_type': {
                            'product_type_code': 'T01',
                            'parent_product_type_code': 'PT01',
                            'product_type_description': 'chuột máy tính',
                            },
                'product_info':{            
                            'product_price': '1100000',
                            'product_color': 'đen',
                            #'product_size': ,
                            'product_description': 'Chuột game không dây Logitech G304 nhẹ, 6 nút lập trình, onboard memory, pin 250h',
                },
                'sale_person_id': 'S01',
                #'promotion': {
                #	'promotion_id': 'KM02',
                #	'promotion_name': 'Giảm 10%',
                #	'time_promotion': '01-05-2022 đến 31-05-2022',
                #	'discount': '10%',
                #	}, 	
                },{
                'product_id': 'P04',
                'product_name': 'Tai nghe Bluetooth Logitech G435',
                'product_type': {
                            'product_type_code': 'T02',
                            'parent_product_type_code': 'PT01',
                            'product_type_description': 'tai nghe',
                            },
                'product_info': {           
                            'product_price': '1500000',
                            'product_color': 'xanh',
                            #'product_size': ,
                            'product_description': 'Tai nghe game không dây Bluetooth Logitech G435 – Mic ảo tích hợp, nhẹ, PC/ Mobile/ PS5',
                },
                'sale_person_id': 'S02',
                'promotion': {
                            'promotion_id': 'KM02',
                            'promotion_name': 'Giảm 10%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '10%',
                            }, 	
                },{
                'product_id': 'P05',
                'product_name': 'Lót chuột cỡ lớn 80x30cm',
                'product_type': {
                            'product_type_code': 'T03',
                            'parent_product_type_code': 'PT01',
                            'product_type_description': 'Lót chuột',
                            },
                'product_info': {            
                            'product_price': '80000',
                            'product_color': 'cam',
                            'product_size': '80x30cm',
                            'product_description': 'Lót chuột cỡ lớn 80x30cm dày dặn 3mm chuyên game chống trơn trượt siêu bền siêu rẻ',
                },
                'sale_person_id': 'S03',
                'promotion': {
                            'promotion_id': 'KM03',
                            'promotion_name': 'Giảm 15%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '15%',
                            }, 	
                },{
                'product_id': 'P06',
                'product_name': 'Áo hoodie',
                'product_type': {
                            'product_type_code': 'T10',
                            'parent_product_type_code': 'PT10',
                            'product_type_description': 'Áo quần',
                            },
                'product_info': {            
                            'product_price': '300000',
                            'product_color': 'trắng',
                            'product_size': 'L',
                            'product_description': 'Áo hoodie essentials, chất liệu nỉ bông cao cấp',
                },
                'sale_person_id': 'S10',
                'promotion': {
                            'promotion_id': 'KM03',
                            'promotion_name': 'Giảm 15%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '15%',
                            }, 	
                },{
                'product_id': 'P07',
                'product_name': 'Mắt kính',
                'product_type': {
                            'product_type_code': 'T11',
                            'parent_product_type_code': 'PT10',
                            'product_type_description': 'Kính',
                            },
                'product_info': {            
                            'product_price': '200000',
                            'product_color': 'đen',
                            #'product_size': 'L',
                            'product_description': 'Mắt kính chống bức xạ phong cách thời trang sành điệu',
                },
                'sale_person_id': 'S10',
                # 'promotion': {
                #             'promotion_id': 'KM03',
                #             'promotion_name': 'Giảm 15%',
                #             'time_promotion': '01-05-2022 đến 31-05-2022',
                #             'discount': '15%',
                #             }, 	
                },{
                'product_id': 'P08',
                'product_name': 'Đồng hồ WISHDOIT',
                'product_type': {
                            'product_type_code': 'T12',
                            'parent_product_type_code': 'PT10',
                            'product_type_description': 'Đồng hồ',
                            },
                'product_info': {                        
                            'product_price': '1500000',
                            'product_color': 'nâu',
                            #'product_size': 'L',
                            'product_description': 'WISHDOIT màu vàng kim dây đeo thép không gỉ/da',
                },
                'sale_person_id': 'S11',
                'promotion': {
                            'promotion_id': 'KM02',
                            'promotion_name': 'Giảm 10%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '10%',
                            }, 	
                },{
                'product_id': 'P09',
                'product_name': 'Lắc tay nữ Eleanor Accessories',
                'product_type': {
                            'product_type_code': 'T13',
                            'parent_product_type_code': 'PT10',
                            'product_type_description': 'Lắc tay',
                            },
                'product_info': {
                            'product_price': '50000',
                            'product_color': 'bạc',
                            #'product_size': 'L',
                            'product_description': 'Lắc tay nữ Eleanor Accessories vòng tay phong cách Hàn Quốc phụ kiện trang sức thời trang đẹp',
                },
                'sale_person_id': 'S11',
                # 'promotion': {
                #             'promotion_id': 'KM02',
                #             'promotion_name': 'Giảm 10%',
                #             'time_promotion': '01-05-2022 đến 31-05-2022',
                #             'discount': '10%',
                #             }, 	
                },{
                'product_id': 'P10',
                'product_name': 'Áo croptop',
                'product_type': {
                            'product_type_code': 'T10',
                            'parent_product_type_code': 'PT10',
                            'product_type_description': 'Quần Áo',
                            },
                'product_info': {
                            'product_price': '120000',
                            'product_color': 'tím',
                            'product_size': 'M',
                            'product_description': 'ÁO CROPTOP POLO NỮ',
                },
                'sale_person_id': 'S12',
                'promotion': {
                            'promotion_id': 'KM01',
                            'promotion_name': 'Giảm 5%',
                            'time_promotion': '01-05-2022 đến 31-05-2022',
                            'discount': '5%',
                            }, 	
                },
        ]
product_info.insert_many(list_products)        