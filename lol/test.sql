select [1], id, col 
from ["./data/data.csv"] 
where [2] = 'test' and age >= 122.5 and age >= 122.5 
group by [3] 
order by id desc, age asc, [4]
limit 100
offset 200;


select *
into ['Data Source=SQL;Initial Catalog=TestDB;Persist Security Info=True;User ID=sa;Password=P@ssw0rd'] from ['D:\\file1.csv']
where [2] = 'test'
and age >= 122.5 ;


select studentName, Phone
from ["Data Source=SQL;Initial Catalog=TestDB;Persist Security Info=True;User ID=sa;Password=P@ssw0rd"]
where Phone like "065%"
group by Phone, StudenName, city;


insert into ["./data/data.csv"] 
(id, name, test) 
values 
('123', 131123, 'dsa');


insert into ["./data/data.csv"] 
select name 
from table
where id = 5 and age > 20 
order by id;


update ["Data Source=SQL;Initial Catalog=TestDB;Persist Security Info=True;User ID=sa;Password=P@ssw0rd"]
set city ="value1", phone="Value2"  where age > 10;


delete from ['D:\file1.csv'] as file
where age > 10;


select Phone, Studentname, city, State, zipcode
from ['D:\file1.csv'] as file1 
    inner join  ['D:\file2.csv'] as file2
    on file1.phone = file2.phone
    left join  ['D:\file4.csv'] as file4
    on file1.phone = file4.phone
where city="Houston"
order by zipcode
