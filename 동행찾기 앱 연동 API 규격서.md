# 동행찾기 앱 연동 API 규격서 v0.01

### [POST]/user : 유저 회원가입

Parameters

UserCreate (body)

{

"name" : "강태형",

"cellphoneNum" : "010-9034-4768",

"email" : "gtpgg1013@gmail.com",

"address" : "경기도 수원시",

"interestedplace1" : "유럽",

"interestedplace2" : "미국",

"picture" : "프로필사진",

"ID" : "gkongkong",

"Password" : "1234!!",

"interested" : "쇼핑",

"style" : "도전"

}

Responses

Code 200 : 회원 정상 등록

{

"createdTime" : "201905052202",

"status" : "succeed"

}



### [GET]/user/DBnum : 유저의 회원가입 내용을 알려준다

Parameters

DBnum(int) : 사용자의 DB상 저장된 번호

Responses

{

"name" : "강태형",

"cellphoneNum" : "010-9034-4768",

"email" : "gtpgg1013@gmail.com",

"address" : "경기도 수원시",

"interestedplace1" : "유럽",

"interestedplace2" : "미국",

"picture" : "프로필사진",

"ID" : "gkongkong",

"interested" : "쇼핑",

"style" : "도전"

}



### [PUT]/user/UserID : 유저의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

UserID : 유저 ID

UserUpdate : 유저 상세내용 수정에 필요한 정보

{

"cellphoneNum" : "010-9034-1111",

"email" : "afsag1013@gmail.com",

"address" : "경기도 용인시",

"interestedplace1" : "아프리카",

"interestedplace2" : "중국",

"picture" : "프로필사진",

"ID" : "gkongkong22",

"interested" : "여성",

"style" : "로맨스"

}

Response : 200

{

"updatedTime" : "201905052214",

"status" : "succeed"

}



### [DELETE]/user/UserID : 유저를 삭제한다 (회원 탈퇴 : 자기 자신만 삭제 가능)

Parameter

UserID : 유저 ID

Response : 200 (삭제 성공) / 404 (조건에 맞는 유저 ID가 없음)



[POST]/posting : 게시물 작성

Parameters

PostingCreate (body)

{

"ID" : "gkongkong",

"interested" : "쇼핑",

"style" : "도전",

"title" : "방콕 2박 3일 동행 구해요",

"contents" : "어디어디에서 어쩌구저쩌구",

"tripdate" : "20190505-20190507",

"destination1" : "태국",

"destination2" : "방콕"

}

Responses

Code 200 : 글 정상 등록

{

"createdTime" : "201905052202",

"status" : "succeed"

}



### [GET]/posting/DBnum : 게시물 상세 내용

Parameters

DBnum(int) : 글의 DB상 저장된 번호

Responses

{

"ID" : "gkongkong",

"interested" : "쇼핑",

"style" : "도전",

"title" : "방콕 2박 3일 동행 구해요",

"contents" : "어디어디에서 어쩌구저쩌구",

"tripdate" : "20190505-20190507",

"destination1" : "태국",

"destination2" : "방콕"

}



### [PUT]/posting/DBnum : 글의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

DBnum : DB상 저장된 글의 번호

UserUpdate : 글 상세내용 수정에 필요한 정보

{

"contents" : "어디어디에서 어쩌구저쩌구 <동행찾았습니다>",

"tripdate" : "20190505-20190507",

"destination1" : "태국",

"destination2" : "방콕"

}

Response : 200

{

"updatedTime" : "201905052239",

"status" : "succeed"

}



### [DELETE]/posting/DBnum : 글을 삭제한다 (글쓴이만 삭제 가능)

Parameter

DBnum : DB상 저장된 글 번호

Response : 200 (삭제 성공) / 404 (조건에 맞는 유저 ID가 없음)



### [GET]/posting/search : 글을 검색한다

Parameter

Interest (String) : 사용자가 검색한 단어 : 중국

tripdate (String) : 사용자가 선택한 여행 시기 : "20190505-20190606"

datetype (boolean) : datetype가 true이면 검색자의 여행 기간이 글쓴이 여행 기간에 전부 포함되게, false이면 여행 기간이 교집합만 있어도 검색 결과 return : false

Response : 200

{

"postingnum" : "2",

"title" : "중국 갈 사람 찾습니다"

"writerID" : "gkongkong",

"interested" : "중국",

"writertripdate" : "20190502-20190508"

}



### [POST]/posting/DBnum/reply : 댓글 달기

Parameter

DBnum : DB상 저장된 글의 번호

ReplyCreate (body)

{

"replyerID" : "dbk",

"replyContents" : "쓰촨성 주변에 계세요?",

"replyTime" : "201905052254"

}

Response : 200

{

"updatedTime" : "201905052254",

"status" : "succeed"

}



### [GET]/posting/DBnum/reply/replynum : DBnum 번호 글에 달린 reply 가져오기

Parameter

DBnum : DB상 저장된 글의 번호

replynum : 답글 번호

Responses : 200

{

"replyerID" : "gkongkong",

"replyContents" : "아뇨, 베이징 쪽에 있을 것 같습니다",

"replyTime" : "201905052257"

}



### [PUT]/posting/DBnum/reply/replynum : 댓글의 상세내용을 수정한다 (자신만 수정할 수 있다)

Parameter

DBnum : DB상 저장된 글의 번호

replynum : 댓글 번호

UserUpdate : 글 상세내용 수정에 필요한 정보

{

"replyContents" : "일정이 바뀌어서 스촨으로 내일 갈 것 같습니다."

}

Response : 200

{

"updatedTime" : "201905052259",

"status" : "succeed"

}



### [DELETE]/posting/DBnum/reply/replynum : 댓글을 삭제한다 (글쓴이만 삭제 가능)

Parameter

DBnum : DB상 저장된 글 번호

replynum : 댓글 번호

Response : 200 (삭제 성공) / 404 (조건에 맞는 유저 ID가 없음)









