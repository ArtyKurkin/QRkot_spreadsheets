from datetime import datetime
from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def close_donation(
        obj_in: Union[CharityProject, Donation],
) -> Union[CharityProject, Donation]:
    obj_in.invested_amount = obj_in.full_amount
    obj_in.fully_invested = True
    obj_in.close_date = datetime.now()
    return obj_in


async def get_not_full_invested(
        obj_in: Union[CharityProject, Donation],
        session: AsyncSession
) -> List[Union[CharityProject, Donation]]:
    db_obj = await session.execute(
        select(obj_in).where(
            obj_in.fully_invested == 0
        ).order_by(obj_in.create_date)
    )
    return db_obj.scalars().all()


async def investing_process(
        obj_in: Union[CharityProject, Donation],
        obj_model: Union[CharityProject, Donation],
        session: AsyncSession,
) -> Union[CharityProject, Donation]:
    not_full_invested_objects = await get_not_full_invested(obj_model, session)
    for object in not_full_invested_objects:
        free_amount_in = obj_in.full_amount - obj_in.invested_amount
        free_amount_object = object.full_amount - object.invested_amount
        if free_amount_in > free_amount_object:
            obj_in.invested_amount += free_amount_object
            await close_donation(object)
        elif free_amount_in == free_amount_object:
            await close_donation(obj_in)
            await close_donation(object)
        else:
            object.invested_amount += free_amount_in
            await close_donation(obj_in)
        session.add(obj_in)
        session.add(object)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in
