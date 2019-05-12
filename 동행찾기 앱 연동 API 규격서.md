# 동행찾기 앱 연동 API 규격서 v0.01

### [POST]/user : 유저 회원가입

Parameters

UserCreate (body)

{

"name" : "강태형",

"cellphoneNum" : "010-9034-4768",

"email" : "gtpgg1013@gmail.com",

"address" : "경기도 수원시",

"interestedPlace1" : "1",

"interestedPlace2" : "2",

"picture" : "프로필사진",

"id" : "gkongkong",

"password" : "1234!!",

"interested" : "2",

"style" : "3"

}

Responses

Code 200 : 회원 정상 등록

{

"createdTime" : "201905052202",

"status" : "succeed"

}



### [GET]/user/{dbNum} : 유저의 회원가입 내용을 알려준다

Parameters

dbNum(int) : 사용자의 DB상 저장된 번호

Responses

{

"name" : "강태형",

"cellphoneNum" : "010-9034-4768",

"email" : "gtpgg1013@gmail.com",

"address" : "경기도 수원시",

"interestedPlace1" : "1",

"interestedPlace2" : "2",

"picture" : "프로필사진",

"id" : "gkongkong",

"interested" : "2",

"style" : "3"

}



### [PUT]/user/{userId} : 유저의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

userId : 유저 ID

UserUpdate : 유저 상세내용 수정에 필요한 정보

{

"cellphoneNum" : "010-9034-1111",

"email" : "afsag1013@gmail.com",

"address" : "경기도 용인시",

"interestedPlace1" : "4",

"interestedPlace2" : "5",

"picture" : "프로필사진",

"id" : "gkongkong22",

"interested" : "3",

"style" : "2"

}

Response : 200

{

"updatedTime" : "201905052214",

"status" : "succeed"

}



### [DELETE]/user/{userId} : 유저를 삭제한다 (회원 탈퇴 : 자기 자신만 삭제 가능)

Parameter

userId : 유저 ID

Response : 200 (삭제 성공) / 404 (조건에 맞는 유저 ID가 없음)



[POST]/posting : 게시물 작성

Parameters

PostingCreate (body)

{

"id" : "gkongkong",

"interested" : "1",

"style" : "2",

"title" : "방콕 2박 3일 동행 구해요",

"contents" : "어디어디에서 어쩌구저쩌구",

"tripDate" : "20190505-20190507",

"interestedPlace1" : "1",

"interestedPlace2" : "2"

}

Responses

Code 200 : 글 정상 등록

{

"deletedTime" : "201905052202",

"status" : "succeed"

}



### [GET]/posting/{dbNum} : 게시물 상세 내용

Parameters

dbNum(int) : 글의 DB상 저장된 번호

Responses

{

"id" : "gkongkong",

"interested" : "2",

"style" : "4",

"title" : "방콕 2박 3일 동행 구해요",

"contents" : "어디어디에서 어쩌구저쩌구",

"tripDate" : "20190505-20190507",

"destination1" : "1",

"destination2" : "2"

}



### [PUT]/posting/{dbNum} : 글의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

dbNum : DB상 저장된 글의 번호

UserUpdate : 글 상세내용 수정에 필요한 정보

{

"contents" : "어디어디에서 어쩌구저쩌구 <동행찾았습니다>",

"tripDate" : "20190505-20190507",

"destination1" : "1",

"destination2" : "2"

}

Response : 200

{

"updatedTime" : "201905052239",

"status" : "succeed"

}



### [DELETE]/posting/{dbNum} : 글을 삭제한다 (글쓴이만 삭제 가능)

Parameter

dbNum : DB상 저장된 글 번호

Response : 200 (삭제 성공) 



### [GET]/posting/search : 글을 검색한다

Parameter

Interest (String) : 사용자가 검색한 단어 : 중국

tripDate (String) : 사용자가 선택한 여행 시기 : "20190505-20190606"

dateType (boolean) : dateType가 true이면 검색자의 여행 기간이 글쓴이 여행 기간에 전부 포함되게, false이면 여행 기간이 교집합만 있어도 검색 결과 return : false

Response : 200

{

"postingNum" : "2",

"title" : "중국 갈 사람 찾습니다"

"writerId" : "gkongkong",

"interested" : "1",

"writerTripDate" : "20190502-20190508"

}



### [POST]/posting/{dbNum}/reply : 댓글 달기

Parameter

dbNum : DB상 저장된 글의 번호

ReplyCreate (body)

{

"replyerId" : "dbk",

"replyContents" : "쓰촨성 주변에 계세요?",

"replyTime" : "201905052254"

}

Response : 200

{

"updatedTime" : "201905052254",

"status" : "succeed"

}



### [GET]/posting/{dbNum}/reply/{replyNum} : dbNum 번호 글에 달린 reply 가져오기

Parameter

dbNum : DB상 저장된 글의 번호

replyNum : 답글 번호

Responses : 200

{

"replyerId" : "gkongkong",

"replyContents" : "아뇨, 베이징 쪽에 있을 것 같습니다",

"replyTime" : "201905052257"

}



### [PUT]/posting/{dbNum}/reply/{replyNum} : 댓글의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

dbNum : DB상 저장된 글의 번호

replyNum : 댓글 번호

UserUpdate : 글 상세내용 수정에 필요한 정보

{

"replyContents" : "일정이 바뀌어서 스촨으로 내일 갈 것 같습니다."

}

Response : 200

{

"updatedTime" : "201905052259",

"status" : "succeed"

}



### [DELETE]/posting/{dbNum}/reply/{replyNum} : 댓글을 삭제한다 (글쓴이만 삭제 가능)

Parameter

dbNum : DB상 저장된 글 번호

replyNum : 댓글 번호

Response : 200 (삭제 성공) 



### [GET]/geolist: 지역 조회

Parameter

Response : 200

{

"geoList" : [

​	{

​		"idx" : "0",

​		"geoAreaName" : "동유럽"

​	},

​	{

​		"idx" : "1",

​		"geoAreaName" : "남유럽",

​		"geoDetailList" : [

​			{

​				"idx" : "0",

​				"geoDetailName" : "이탈리아"

​			},

​			{

​				"idx" : "1",

​				"geoDetailName" : "스페인"

​			},

​			{

​				"idx" : "2",

​				"geoDetailName" : "터키"

​			},

​			{

​				"idx" : "3",

​				"geoDetailName" : "그리스"

​			},

​			{

​				"idx" : "0",

​				"geoDetailName" : "포르투갈"

​			},

​			{

​				"idx" : "4",

​				"geoDetailName" : "루마니아"

​			},

​			{

​				"idx" : "5",

​				"geoDetailName" : "크로아티아"

​			},

​			{

​				"idx" : "6",

​				"geoDetailName" : "불가리아"

​			},

​			{

​				"idx" : "7",

​				"geoDetailName" : "슬로베니아"

​			},

​			{

​				"idx" : "8",

​				"geoDetailName" : "세르비아"

​			},

​		]

​	},

​	{

​	"idx" : "2",

​	"geoAreaName" : "북유럽",

​	"geoDetailList" : [

​			{

​				"idx" : "9",

​				"geoDetailName" : "네덜란드"

​			},

​			{

​				"idx" : "10",

​				"geoDetailName" : "독일"

​			},

​			{

​				"idx" : "11",

​				"geoDetailName" : "노르웨이"

​			},

​			{

​				"idx" : "12",

​				"geoDetailName" : "덴마크"

​			},

​			{

​				"idx" : "13",

​				"geoDetailName" : "스웨덴"

​			},

​			{

​				"idx" : "14",

​				"geoDetailName" : "아이슬란드"

​			},

​			{

​				"idx" : "15",

​				"geoDetailName" : "핀란드"

​			},

​			{

​				"idx" : "16",

​				"geoDetailName" : "발트 3국"

​			}

​		]

​	},

​	{

​	"idx" : "3",

​	"geoAreaName" : "북미",

​	"geoDetailList" : [

​			{

​				"idx" : "17",

​				"geoDetailName" : "미국"

​			},

​			{

​				"idx" : "18",

​				"geoDetailName" : "캐나다"

​			},

​			{

​				"idx" : "19",

​				"geoDetailName" : "멕시코"

​			},

​			{

​				"idx" : "20",

​				"geoDetailName" : "그린란드",

​			}

​		]

​	},

​	{

​	"idx" : "4",

​	"geoAreaName" : "남미",

​	"geoDetailList" : [

​			{

​				"idx" : "21",

​				"geoDetailName" : "우루과이"

​			},

​			{

​				"idx" : "22",

​				"geoDetailName" : "칠레"

​			},

​			{

​				"idx" : "23",

​				"geoDetailName" : "콜롬비아"

​			},

​			{

​				"idx" : "24",

​				"geoDetailName" : "파라과이"

​			},

​			{

​				"idx" : "25",

​				"geoDetailName" : "페루"

​			},

​			{

​				"idx" : "26",

​				"geoDetailName" : "볼리비아"

​			},

​			{

​				"idx" : "27",

​				"geoDetailName" : "브라질"

​			},

​			{

​				"idx" : "28",

​				"geoDetailName" : "아르헨티나"

​			},

​			{

​				"idx" : "29",

​				"geoDetailName" : "에콰도르"

​			},

​			{

​				"idx" : "30",

​				"geoDetailName" : "그외"

​			}

​		]

​	},

​	{

​		"idx" : "5",

​		"geoAreaName" : "동아시아",

​		"geoDetailList" : [

​			{

​				"idx" : "31",

​				"geoDetailName" : "일본"

​			},

​			{

​				"idx" : "32",

​				"geoDetailName" : "중국"

​			},

​			{

​				"idx" : "33",

​				"geoDetailName" : "홍콩"

​			},

​			{

​				"idx" : "34",

​				"geoDetailName" : "대만"

​			},

​			{

​				"idx" : "35",

​				"geoDetailName" : "몽골"

​			},

​			{

​				"idx" : "36",

​				"geoDetailName" : "그외"

​			}

​		]

​	},

​	{

​		"idx" : "6",

​		"geoAreaName" : "동남아시아",

​		"geoDetailList" : [

​			{

​				"idx" : "37",

​				"geoDetailName" : "말레이시아"

​			},

​			{

​				"idx" : "38",

​				"geoDetailName" : "미얀마"

​			},

​			{

​				"idx" : "39",

​				"geoDetailName" : "베트남"

​			},

​			{

​				"idx" : "40",

​				"geoDetailName" : "싱가포르"

​			},

​			{

​				"idx" : "41",

​				"geoDetailName" : "브루나이"

​			},

​			{

​				"idx" : "42",

​				"geoDetailName" : "인도네시아"

​			},

​			{

​				"idx" : "43",

​				"geoDetailName" : "캄보디아"

​			},

​			{

​				"idx" : "44",

​				"geoDetailName" : "태국"

​			},

​			{

​				"idx" : "45",

​				"geoDetailName" : "필리핀"

​			},

​			{

​				"idx" : "46",

​				"geoDetailName" : "그외"

​			}

​		]

​	},

​	{

​		"idx" : "7",

​		"geoAreaName" : "서남아시아",

​		"geoDetailList" : [

​			{

​				"idx" : "47",

​				"geoDetailName" : "사우디아라비아"

​			},

​			{

​				"idx" : "48",

​				"geoDetailName" : "요르단"

​			},

​			{

​				"idx" : "49",

​				"geoDetailName" : "이라크"

​			},

​			{

​				"idx" : "50",

​				"geoDetailName" : "이란"

​			},

​			{

​				"idx" : "51",

​				"geoDetailName" : "이스라엘"

​			},

​			{

​				"idx" : "52",

​				"geoDetailName" : "쿠웨이트"

​			},

​			{

​				"idx" : "53",

​				"geoDetailName" : "이집트"

​			},

​			{

​				"idx" : "54",

​				"geoDetailName" : "그외"

​			}

​		]

​	},

​	{

​		"idx" : "8",

​		"geoAreaName" : "오세아니아",

​		 "geoDetailList" : [

​			{

​				"idx" : "55",

​				"geoDetailName" : "호주"

​			},

​			{

​				"idx" : "56",

​				"geoDetailName" : "뉴질랜드"

​			},

​			{

​				"idx" : "57",

​				"geoDetailName" : "그외"

​			}

​			]

​	},

​	{

​		"idx" : "9",

​		"geoAreaName" : "그외",

​		 "geoDetailList" : [

​			{

​				"idx" : "58",

​				"geoDetailName" : "그외"

​			}

​			]

​	}

​	]



}









