<div align="center">
  <a href="http://hutoryanin.ru/">
    <img src="https://github.com/ogneyar/Hutoryanin/tree/master/web/static/logo.png" width="492" height="228">
  </a>
  <br>
  <br>
	<a href="https://hutoryanin.ru/products/">
		<!-- <img src=""> -->
        Товары
	</a>
	<a href="https://hutoryanin.ru/public/1/">
		<!-- <img src=""> -->
        Публикации
	</a>
  <br>
  <br>
</div>

# ХуторянинЪ

Тест typeORM:

```typescript
import {Entity, PrimaryGeneratedColumn, Column} from "typeorm";

@Entity()
export class User {

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    firstName: string;

    @Column()
    lastName: string;

    @Column()
    age: number;

}
```