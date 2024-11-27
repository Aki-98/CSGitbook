## 1. **Test One Thing at a Time in Isolation**

每个Test case 只测试一种情况，只应该依赖于Mocks和Stubs，不应该依赖于其他测试的结果甚至网络。

## 2. **Follow the AAA Rule: Arrange, Act, Assert**

Arrange:  Set variables, fields, and properties to enable the test to be run, as well as define the expected result.

Act:  Call the method that you are testing.

Assert: Call the testing framework to verify that the result of your “Act” is what was expected.

## **3. Write Simple “Fastball-Down-the-Middle” Tests First**

首先设计最简单的TestCase，可以清晰地体现程序的功能和结构的，然后才开始测试程序的边界与异常

## **4. Test Across Boundaries**

设计一些跨越边界的Case，比如在对日期或时间的程序进行测试时，设计时间跳转的Case。设计一些可能使你的程序Fail或者表现异常的Case

## **5. If You Can, Test the Entire Spectrum**

如果可能的话，测试程序功能中所有的可能性。

## **6. If Possible, Cover Every Code Path**

如果可能的话，覆盖每一条程序语句/分支，最好能使用UT覆盖率工具检查查看

## **7. Write Tests That Reveal a Bug, Then Fix It**

如果在编写测试中发现了Bug，那么就修复这个Bug，同时这个测试能够成为一个更好的回归（Regression）测试Case，以便之后快速定位这个Bug

## **8. Make Each Test Independent**

合理地运用SetUp和TearDown，确保每个TestCase都可以独立地运行

## **9. Name Your Tests Clearly and Don’t Be Afraid of Long Names**

为每条测试Case起明确清晰的名字，不要担心过长的名字。

名字可以参考：TestDivisionWhenNumPositiveDenomNegative、DivisionByZeroShouldThrowException

## **10. Test That Every Raised Exception Is Raised**

编写测试确保你的代码引发的每个异常确实在适当的情况下被引发。

## **11. Avoid the Use of Assert.IsTrue**

不要这样写-->Assert.IsTrue(Expected = Actual);

改成这样-->Assert.AreEqual(Expected, Actual)

## **12. Constantly Run Your Tests**

一边编写新代码，一边跑测试Case

## **13. Run Your Tests as Part of Every Automated Build**

将UT Case包含在自动化集成中，如果test fail，应该立即修复
