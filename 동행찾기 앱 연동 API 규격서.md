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

"destination1" : "태국",

"destination2" : "방콕"

}

Responses

Code 200 : 글 정상 등록

{

"createdTime" : "201905052202",

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

"destination1" : "태국",

"destination2" : "방콕"

}



### [PUT]/posting/{dbNum} : 글의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

dbNum : DB상 저장된 글의 번호

UserUpdate : 글 상세내용 수정에 필요한 정보

{

"contents" : "어디어디에서 어쩌구저쩌구 <동행찾았습니다>",

"tripDate" : "20190505-20190507",

"destination1" : "태국",

"destination2" : "방콕"

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









