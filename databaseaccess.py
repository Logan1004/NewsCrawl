create table CompanyInfo
(
	Company varchar(40) null,
	Url varchar(1000) null,
	Category varchar(200) null
)
;

create table InfoTable
(
	Company varchar(40) null,
	Url varchar(1000) null,
	Category varchar(200) null,
	Content varchar(100) null
)
;

create table WebInfo
(
	Company varchar(40) not null
		primary key,
	Content longtext not null
)
;

