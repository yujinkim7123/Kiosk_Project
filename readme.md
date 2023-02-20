## 깃

### 브랜치 전략

```
┣ master
┃┣ develop
┃┃┣ feature
```

feature/{기능 상세}

### 컨벤션

| Tag Name | Description                                                  |
| -------- | ------------------------------------------------------------ |
| Feat     | 새로운 기능을 추가                                           |
| Fix      | 버그 수정                                                    |
| Design   | CSS 등 사용자 UI 디자인 변경                                 |
| Refactor | 프로덕션 코드 리팩토링                                       |
| Comment  | 필요한 주석 추가 및 변경                                     |
| Docs     | 문서 수정                                                    |
| Test     | 테스트 코드, 리펙토링 테스트 코드 추가, Production Code(실제로 사용하는 코드) 변경 없음 |
| Rename   | 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우           |
| Remove   | 파일을 삭제하는 작업만 수행한 경우                           |

`git commit -m '{TAG} {커밋 메세지}'`

