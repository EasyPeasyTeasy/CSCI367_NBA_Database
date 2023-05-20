create table if not exists cpi (
    /*
    example:
        id,full_name,first_name,last_name,is_active
        76001,Alaa Abdelnaby,Alaa,Abdelnaby,0
 */

    id int primary key,
    full_name text not null,
    first_name text not null,
    last_name text not null,
    is_active int
)