-- 코드를 입력하세요
SELECT ugb.TITLE, ugb.BOARD_ID, ugr.REPLY_ID, ugr.WRITER_ID, ugr.CONTENTS, TO_CHAR(ugr.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE 
FROM  USED_GOODS_REPLY ugr JOIN USED_GOODS_BOARD ugb
ON ugb.BOARD_ID = ugr.BOARD_ID WHERE TRUNC(ugb.CREATED_DATE, 'MM') = DATE '2022-10-01'
ORDER BY ugr.CREATED_DATE, ugb.TITLE;
