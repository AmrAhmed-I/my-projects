import 'dart:io';

void main(){

 stdout.writeln("Hello World");

 stdout.writeln("Enter your name: ");
 String name1 = stdin.readLineSync()!;
 print("Hello, $name1");

String name = "Amr";

print(name.toUpperCase());//*تحويل الحروف الى حروف كبيرة
print(name.toLowerCase());//*تحويل الحروف الى حروف صغيرة
print(name.contains("A"));//*تحقق من وجود الحرف A في الاسم 
print(name.startsWith("A"));//*تحقق من أن الاسم يبدأ بحرف A
print(name.endsWith("r"));//*تحقق من أن الاسم ينتهي بحرف r
print(name.replaceAll("Amr", "Ali")); //*استبدال الاسم Amr بالاسم Ali
print(name.substring(0, 2));//*طباعة جزء من الاسم من الحرف 0 الى الحرف 2
print(name.trim());  // *حذف المسافات

double number = 15.7;

number.round();   //? تقريب
number.floor();   //? تقريب لأسفل
number.ceil();    //? تقريب لأعلى
number.abs();     //? القيمة المطلقة

int number2 = 100;

number2.isEven;  //? تحقق من أن الرقم زوجي
number2.isOdd;   //? تحقق من أن الرقم فردي
number2.toString();  //? تحويل الرقم الى نص

}