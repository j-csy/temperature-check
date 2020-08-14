/****** Object:  Table [dbo].[data_tst]    Script Date: 14/08/2020 8:01:40 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[data_tst](
	[EventId] [varchar](50) NULL,
	[DeviceId] [varchar](50) NULL,
	[Name] [varchar](50) NULL,
	[Epoch] [numeric](20, 0) NULL
) ON [PRIMARY]
GO


WITH MyData AS
(
SELECT
[DeviceId],
RowSeq = row_number() 
OVER (PARTITION BY [DeviceId] ORDER BY [Epoch])
, [Epoch]
, cast ([Epoch] as BIGINT) as epochbigint
, [Name]
FROM [data_tst]
where [Name] in ('start','stop')
)
SELECT ---- Show two consecutive states next to each other
SiteCode = A.[DeviceId]
, FromStatus = A.[Name]
, ToStatus = B.[Name]
, FromTime = A.[epochbigint]
, ToTime = B.[epochbigint]
 , (B.[epochbigint]  - A.[epochbigint]) as epochDiff
 ,  (B.[epochbigint]  - A.[epochbigint]) / 60 as epochDiffsecs 
FROM MyData AS A 
JOIN MyData AS B ON A.RowSeq = B.RowSeq-1 AND A.[DeviceId] = B.[DeviceId]
WHERE A.[Name]= 'start'
ORDER BY A.[DeviceId], A.RowSeq
;

