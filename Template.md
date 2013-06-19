# Invoice - <$Date>
---------------------------------------	
	
Developer: <$Name> <br>
Contact Email: <$Email> <br>
Phone: <$Phone> <br>
Website: <$Website> <br>

<$Address>
	
## Summary

Task/Payment Description                 | Hrs    | Hr. Cost  | Subtotal 
:----------------------------------------| ------ | --------- | --------
<$TaskHeader>$Task,$Hours,$HourlyRate,$TaskSubtotal
<$TaskTable> 

*Total Hours:* <$TotalHours> *Sub Total*: <$Subtotal> / **Grand Total:** <$GrandTotal> (no tax)

## Payments
Payment Description                       | Date      | Amount | Previous Total | Remaining Total
:---------------------------------------- | --------- | ------ | -------------- | ---------------
<$PaymentHeader>$Payment,$Date,$Amount,$PreviousTotal,$RemainingTotal
<$PaymentTable>

------------------------------------------
## Total Payment Due: <$TotalDue>
------------------------------------------