"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass
class Commission(ABC):
    """Represents a generic comission."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute the comission to be paid out."""


@dataclass
class ContractCommission(Commission):
    """Represents a comission."""

    comission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """Compute the comission to be paid out."""
        return self.comission * self.contracts_landed


@dataclass
class Contract(ABC):
    """Represents a contract and a payment proces for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee nder this contract."""


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    comission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the emplyee should be paid."""
        payout = self.contract.get_payment()
        if self.comission is not None:
            payout += self.comission.get_payment()
        return payout


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    """Contract type for an employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelanceContract(Contract):
    """Contract type for an employee that's paid based on freelancer basis."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)

    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah",
        id=47832,
        contract=sarah_contract,
        comission=sarah_commission
    )
    print(
        f"{sarah.name} landed {sarah.comission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
